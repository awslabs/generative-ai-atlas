// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

// Standard Analytics Event Format
class StandardEventFormatter {
    constructor(sessionId, amplifyIdentityId) {
        this.sessionId = sessionId;
        this.amplifyIdentityId = amplifyIdentityId;
    }

    createStandardEvent(eventType, eventData = {}) {
        return {
            eventType,
            sessionId: this.sessionId,
            amplifyIdentityId: this.amplifyIdentityId,
            timestamp: new Date().toISOString(),
            url: window.location.href,
            userAgent: navigator.userAgent,
            eventData
        };
    }

    pageView(previous = null) {
        return this.createStandardEvent('pageView', {
            section: window.location.pathname,
            previous: previous || document.referrer,
            title: document.title
        });
    }

    click(element) {
        return this.createStandardEvent('click', {
            href: element.href,
            text: element.textContent?.trim(),
            isExternal: element.hostname !== window.location.hostname,
            tagName: element.tagName,
            className: element.className
        });
    }

    scroll(depth) {
        return this.createStandardEvent('scroll', {
            depth,
            maxDepth: depth
        });
    }

    timeOnPage(duration) {
        return this.createStandardEvent('timeOnPage', {
            duration,
            unit: 'seconds'
        });
    }
}

/**
 * Analytics tracking module with improved structure and error handling
 */
class AnalyticsTracker {
    constructor() {
        this.sessionId = null;
        this.amplifySessionId = null;
        this.lastUrl = null;
        this.maxScroll = 0;
        this.startTime = Date.now();
        this.initialized = false;
        this.unloadEventSent = false;           // Prevent duplicate unload events
        this.sentEvents = new Set();            // Track sent events to prevent duplicates
        this.localStorageAvailable = null;      // Cache localStorage availability check

        this.config = {
            aws_project_region: "us-west-2",
            aws_cognito_identity_pool_id: "us-west-2:451df9c6-9567-42c9-b20a-f3686fb4fd0e",
            aws_cognito_region: "us-west-2",
            aws_kinesis_firehose_stream_name: "GenAIAtlasAnalytics-Service-prod-ClickstreamKinesis-Ye0sQYCyuaRz",
        };
    }

    generateSessionId() {
        if (!this.sessionId) {
            try {
                this.sessionId = `session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
            } catch (error) {
                console.error('Failed to generate session ID:', error);
            }
        }
        return this.sessionId;
    }

    async getAmplifySessionId() {
        if (!this.amplifySessionId && window.aws_amplify?.Auth) {
            try {
                const credentials = await window.aws_amplify.Auth.currentCredentials();
                this.amplifySessionId = credentials.identityId;
            } catch (error) {
                console.error('Failed to get Amplify identity:', error);
            }
        }
    }

    getEventFormatter() {
        if (!this.eventFormatter && this.sessionId && this.amplifySessionId) {
            this.eventFormatter = new StandardEventFormatter(this.sessionId, this.amplifySessionId);
        }
        return this.eventFormatter;
    }

    cleanEventForFirehose(event) {
        // Remove cache tracking properties before sending to Firehose
        const { storedAt, retryCount, eventKey, ...cleanEvent } = event;
        return cleanEvent;
    }

    async sendEvent(event) {
        if (!event || !window.aws_amplify?.Analytics) return;

        // Check for duplicates (crucial for retry logic)
        const eventKey = this.generateEventKey(event);
        if (this.wasEventSent(eventKey)) {
            console.log('Event already sent, skipping duplicate');
            return;
        }

        try {
            // Clean event data before sending to Firehose
            const cleanEvent = this.cleanEventForFirehose(event);
            
            await window.aws_amplify.Analytics.record({
                data: cleanEvent,
                streamName: this.config.aws_kinesis_firehose_stream_name
            }, 'AWSKinesisFirehose');
            
            // Mark as successfully sent (session + cross-session)
            this.addToSentEvents(eventKey);
            console.log('Event sent successfully');
        } catch (error) {
            console.error('Failed to send analytics event:', error);
            throw error; // Re-throw for retry logic
        }
    }

    trackNavigation() {
        this.lastUrl = location.href;
        const observer = new MutationObserver(() => {
            const url = location.href;
            if (url !== this.lastUrl) {
                const formatter = this.getEventFormatter();
                if (formatter) {
                    // ALL events use localStorage backup - navigation is high risk
                    this.sendEventReliably(formatter.pageView(this.lastUrl), true);
                }
                this.lastUrl = url;
            }
        });
        observer.observe(document, { subtree: true, childList: true });
    }

    trackClicks() {
        document.addEventListener('click', (e) => {
            const link = e.target.closest('a');
            if (link) {
                const formatter = this.getEventFormatter();
                if (formatter) {
                    const clickEvent = formatter.click(link);
                    
                    // ALL click events use localStorage backup - all events are high risk
                    this.sendEventReliably(clickEvent, true);
                    
                    // Check if this click will cause navigation
                    const willNavigate = this.willCauseNavigation(link);
                    
                    if (willNavigate) {
                        // Small delay to give the request a chance to start
                        // before navigation begins (only for same-origin links)
                        if (!clickEvent.eventData.isExternal && !e.ctrlKey && !e.metaKey && !e.shiftKey) {
                            e.preventDefault();
                            setTimeout(() => {
                                window.location.href = link.href;
                            }, 100); // 100ms delay
                        }
                    }
                }
            }
        });
    }

    trackScroll() {
        document.addEventListener('scroll', () => {
            const percent = Math.round((window.scrollY + window.innerHeight) /
                document.documentElement.scrollHeight * 100);
            if (percent > this.maxScroll) {
                this.maxScroll = percent;
                if (percent % 25 === 0) {
                    const formatter = this.getEventFormatter();
                    if (formatter) {
                        // ALL events use localStorage backup - scroll events are high risk
                        this.sendEventReliably(formatter.scroll(percent), true);
                    }
                }
            }
        });
    }

    setupUnloadHandling() {
        const handleUnload = () => {
            // Prevent duplicate unload events
            if (this.unloadEventSent) return;
            this.unloadEventSent = true;
            
            const timeOnPage = Math.round((Date.now() - this.startTime) / 1000);
            const formatter = this.getEventFormatter();
            
            if (formatter) {
                const finalEvent = formatter.timeOnPage(timeOnPage);
                
                // Use localStorage-first strategy for unload events (high risk of cancellation)
                this.sendEventReliably(finalEvent, true);
            }
        };

        // Use pagehide (more reliable than beforeunload) as primary event
        window.addEventListener('pagehide', handleUnload);
        
        // Keep beforeunload as secondary
        window.addEventListener('beforeunload', handleUnload);
        
        // Handle visibility change (mobile browsers, tab switching)
        document.addEventListener('visibilitychange', () => {
            if (document.visibilityState === 'hidden') {
                handleUnload();
            }
        });
    }

    sendEventReliably(event, useLocalStorageBackup = false) {
        if (!event || !window.aws_amplify?.Analytics) return;
        
        const eventKey = this.generateEventKey(event);
        
        // Always check for duplicates first (cross-session)
        if (this.wasEventSent(eventKey)) {
            console.log('Event already processed, skipping');
            return;
        }
        
        if (useLocalStorageBackup) {
            // Strategy 1: localStorage-first (for risky events like navigation/unload)
            // Store first, then mark as sent to prevent race condition duplicates
            this.storeEventLocally(event);
            
            // Mark as being sent IMMEDIATELY to prevent retries during navigation
            this.addToSentEvents(eventKey);
            
            // Clean event data before sending to Firehose
            const cleanEvent = this.cleanEventForFirehose(event);
            
            window.aws_amplify.Analytics.record({
                data: cleanEvent,
                streamName: this.config.aws_kinesis_firehose_stream_name
            }, 'AWSKinesisFirehose').then(() => {
                console.log('Event sent successfully, removing from localStorage');
                this.removeEventFromLocal(event);
            }).catch(error => {
                console.error('Failed to send event, keeping in localStorage for retry:', error);
                // Remove from sent tracking on failure so it can be retried
                this.sentEvents.delete(eventKey);
                // Also remove from localStorage tracking to allow retry
                if (this.isLocalStorageAvailable()) {
                    try {
                        const key = 'analytics_sent_events';
                        const stored = localStorage.getItem(key);
                        if (stored) {
                            const sentEvents = JSON.parse(stored);
                            const filtered = sentEvents.filter(key => key !== eventKey);
                            localStorage.setItem(key, JSON.stringify(filtered));
                        }
                    } catch (e) {
                        console.error('Failed to remove failed event from sent tracking:', e);
                    }
                }
            });
            
        } else {
            // Strategy 2: Direct send only (for safe events like regular clicks/scrolls)
            // Mark as being sent to prevent duplicates
            this.addToSentEvents(eventKey);
            
            // Clean event data before sending to Firehose
            const cleanEvent = this.cleanEventForFirehose(event);
            
            window.aws_amplify.Analytics.record({
                data: cleanEvent,
                streamName: this.config.aws_kinesis_firehose_stream_name
            }, 'AWSKinesisFirehose').then(() => {
                console.log('Event sent successfully');
            }).catch(error => {
                console.error('Failed to send event:', error);
                // Remove from sent tracking on failure to allow potential retry
                this.sentEvents.delete(eventKey);
                // Also remove from localStorage tracking to allow retry
                if (this.isLocalStorageAvailable()) {
                    try {
                        const key = 'analytics_sent_events';
                        const stored = localStorage.getItem(key);
                        if (stored) {
                            const sentEvents = JSON.parse(stored);
                            const filtered = sentEvents.filter(key => key !== eventKey);
                            localStorage.setItem(key, JSON.stringify(filtered));
                        }
                    } catch (e) {
                        console.error('Failed to remove failed event from sent tracking:', e);
                    }
                }
            });
        }
    }

    isLocalStorageAvailable() {
        // Cache the result to avoid repeated checks
        if (this.localStorageAvailable !== null) {
            return this.localStorageAvailable;
        }
        
        try {
            const testKey = '__analytics_test__';
            localStorage.setItem(testKey, 'test');
            localStorage.removeItem(testKey);
            this.localStorageAvailable = true;
        } catch (error) {
            console.warn('localStorage not available:', error.message);
            this.localStorageAvailable = false;
        }
        
        return this.localStorageAvailable;
    }

    generateEventKey(event) {
        // Create a unique key for event deduplication
        // Based on event type, timestamp, and key content
        const keyData = {
            type: event.eventType,
            timestamp: event.timestamp,
            url: event.url,
            sessionId: event.sessionId
        };
        
        if (event.eventType === 'click') {
            keyData.href = event.eventData?.href;
        } else if (event.eventType === 'timeOnPage') {
            keyData.duration = event.eventData?.duration;
        }
        
        return JSON.stringify(keyData);
    }

    // Track successfully sent events across sessions
    addToSentEvents(eventKey) {
        this.sentEvents.add(eventKey);
        
        // Manage memory usage - keep only last 100 events in memory
        if (this.sentEvents.size > 100) {
            // Convert to array, remove first 20, convert back to Set
            const eventArray = Array.from(this.sentEvents);
            eventArray.splice(0, 20); // Remove oldest 20 events
            this.sentEvents = new Set(eventArray);
        }
        
        // Also store in localStorage for cross-session deduplication
        if (this.isLocalStorageAvailable()) {
            try {
                const key = 'analytics_sent_events';
                const stored = localStorage.getItem(key);
                const sentEvents = stored ? JSON.parse(stored) : [];
                
                if (!sentEvents.includes(eventKey)) {
                    sentEvents.push(eventKey);
                    
                    // Keep only last 100 sent events to match in-memory limit
                    if (sentEvents.length > 100) {
                        sentEvents.splice(0, 20); // Remove oldest 20 events when limit exceeded
                    }
                    
                    localStorage.setItem(key, JSON.stringify(sentEvents));
                }
            } catch (error) {
                console.error('Failed to store sent event key:', error);
            }
        }
    }

    // Check if event was already sent (session + cross-session)
    wasEventSent(eventKey) {
        // Check session-level first
        if (this.sentEvents.has(eventKey)) {
            return true;
        }
        
        // Check cross-session in localStorage
        if (this.isLocalStorageAvailable()) {
            try {
                const key = 'analytics_sent_events';
                const stored = localStorage.getItem(key);
                const sentEvents = stored ? JSON.parse(stored) : [];
                return sentEvents.includes(eventKey);
            } catch (error) {
                console.error('Failed to check sent events:', error);
                return false;
            }
        }
        
        return false;
    }

    storeEventLocally(event) {
        // Check if localStorage is available first
        if (!this.isLocalStorageAvailable()) {
            console.warn('localStorage not available, event backup skipped');
            return;
        }
        
        try {
            const eventKey = this.generateEventKey(event);
            
            // Check if we've already processed this exact event
            if (this.sentEvents.has(eventKey)) {
                console.log('Event already processed, skipping storage');
                return;
            }
            
            const key = 'analytics_pending_events';
            const stored = localStorage.getItem(key);
            const events = stored ? JSON.parse(stored) : [];
            
            // Check if this event is already stored
            const isDuplicate = events.some(storedEvent => 
                this.generateEventKey(storedEvent) === eventKey
            );
            
            if (isDuplicate) {
                console.log('Event already stored locally, skipping');
                return;
            }
            
            // Add timestamp for cleanup and retry logic
            events.push({
                ...event,
                storedAt: Date.now(),
                retryCount: 0,
                eventKey: eventKey
            });
            
            // Keep only last 10 events to avoid localStorage bloat
            if (events.length > 10) {
                events.splice(0, events.length - 10);
            }
            
            localStorage.setItem(key, JSON.stringify(events));
            console.log('Event stored locally for retry');
        } catch (error) {
            console.error('Failed to store event locally:', error);
        }
    }

    sendEventWithKeepAlive(event) {
        if (!event || !window.aws_amplify?.Analytics) return;
        
        try {
            const eventKey = this.generateEventKey(event);
            
            // Check if we've already sent this exact event (cross-session)
            if (this.wasEventSent(eventKey)) {
                console.log('Event already sent, skipping');
                return;
            }
            
            // Clean event data before sending to Firehose
            const cleanEvent = this.cleanEventForFirehose(event);
            
            // Use Amplify's record method but without await to avoid blocking unload
            // The keepalive behavior is handled by Amplify's fetch implementation
            window.aws_amplify.Analytics.record({
                data: cleanEvent,
                streamName: this.config.aws_kinesis_firehose_stream_name
            }, 'AWSKinesisFirehose').then(() => {
                console.log('Unload event sent successfully');
                // Mark as successfully sent (session + cross-session)
                this.addToSentEvents(eventKey);
                // Remove from localStorage if it was stored
                this.removeEventFromLocal(event);
            }).catch(error => {
                console.error('Failed to send unload event:', error);
                // Don't mark as sent on failure - allow retry
                // Event remains in localStorage for retry on next session
            });
        } catch (error) {
            console.error('Failed to initiate unload event send:', error);
        }
    }

    removeEventFromLocal(sentEvent) {
        if (!this.isLocalStorageAvailable()) return;
        
        try {
            const key = 'analytics_pending_events';
            const stored = localStorage.getItem(key);
            if (!stored) return;
            
            const events = JSON.parse(stored);
            const filtered = events.filter(event => 
                !(event.eventType === sentEvent.eventType && 
                  event.timestamp === sentEvent.timestamp)
            );
            
            if (filtered.length !== events.length) {
                localStorage.setItem(key, JSON.stringify(filtered));
            }
        } catch (error) {
            console.error('Failed to remove event from localStorage:', error);
        }
    }

    retryPendingEvents() {
        if (!this.isLocalStorageAvailable()) return;
        
        try {
            const key = 'analytics_pending_events';
            const stored = localStorage.getItem(key);
            if (!stored) return;
            
            const events = JSON.parse(stored);
            const now = Date.now();
            const retryableEvents = events.filter(event => {
                // Retry events that are less than 5 seconds old and have less than 3 retries
                const isRecent = now - event.storedAt < 5 * 1000;
                const canRetry = event.retryCount < 3;
                return isRecent && canRetry;
            });
            
            retryableEvents.forEach(async (event) => {
                try {
                    await this.sendEvent(event);
                    this.removeEventFromLocal(event);
                    console.log('Retry successful for stored event');
                } catch (error) {
                    console.error('Retry failed for stored event:', error);
                    // Increment retry count
                    event.retryCount++;
                }
            });
            
            // Clean up old/failed events (older than 5 seconds OR 3+ retries)
            const freshEvents = events.filter(event => 
                now - event.storedAt < 5 * 1000 && event.retryCount < 3
            );
            
            if (freshEvents.length !== events.length) {
                if (freshEvents.length === 0) {
                    localStorage.removeItem(key);
                } else {
                    localStorage.setItem(key, JSON.stringify(freshEvents));
                }
                console.log(`Discarded ${events.length - freshEvents.length} stale analytics events (>5s old)`);
            }
            
        } catch (error) {
            console.error('Failed to retry pending events:', error);
        }
    }

    willCauseNavigation(link) {
        if (!link || !link.href) return false;
        
        try {
            // Check if it's a valid navigation link
            const linkUrl = new URL(link.href, window.location.href);
            
            // Skip non-http protocols
            if (!linkUrl.protocol.startsWith('http')) {
                return false;
            }
            
            // Skip fragment-only links (same page)
            if (linkUrl.pathname === window.location.pathname && 
                linkUrl.search === window.location.search && 
                linkUrl.hash !== '') {
                return false;
            }
            
            // Skip links with download attribute
            if (link.hasAttribute('download')) {
                return false;
            }
            
            // Skip links with target="_blank" or target="_self" with modifier keys
            if (link.target === '_blank') {
                return false;
            }
            
            // Skip links with special attributes that prevent navigation
            if (link.hasAttribute('onclick') && link.getAttribute('onclick').includes('preventDefault')) {
                return false;
            }
            
            // This will cause navigation
            return true;
            
        } catch (error) {
            console.error('Error checking navigation:', error);
            // Default to assuming navigation will happen
            return true;
        }
    }

    setupPeriodicCleanup() {
        // Clean up old localStorage events every 10 seconds
        const cleanupInterval = setInterval(() => {
            if (!this.isLocalStorageAvailable()) return;
            
            try {
                const key = 'analytics_pending_events';
                const stored = localStorage.getItem(key);
                if (!stored) return;
                
                const events = JSON.parse(stored);
                const now = Date.now();
                
                // Remove events older than 5 seconds OR with 3+ failed attempts
                const freshEvents = events.filter(event => {
                    const isRecent = now - event.storedAt < 5 * 1000;
                    const canRetry = event.retryCount < 3;
                    return isRecent && canRetry;
                });
                
                // Only update if we removed some events
                if (freshEvents.length !== events.length) {
                    if (freshEvents.length === 0) {
                        localStorage.removeItem(key);
                        console.log('localStorage analytics events cleared (empty)');
                    } else {
                        localStorage.setItem(key, JSON.stringify(freshEvents));
                        console.log(`localStorage analytics events cleaned: ${events.length - freshEvents.length} stale events removed (>5s old)`);
                    }
                }
            } catch (error) {
                console.error('Failed to perform periodic cleanup:', error);
            }
        }, 10 * 1000); // 10 seconds
        
        // Clean up interval on page unload
        window.addEventListener('beforeunload', () => {
            clearInterval(cleanupInterval);
        });
    }

    async flushPendingEvents() {
        if (!window.aws_amplify?.Analytics?.flushEvents) return false;
        
        try {
            await Promise.race([
                window.aws_amplify.Analytics.flushEvents(),
                new Promise((_, reject) => 
                    setTimeout(() => reject(new Error('Flush timeout')), 2000)
                )
            ]);
            return true;
        } catch (error) {
            console.error('Failed to flush events:', error);
            return false;
        }
    }

    // Initialize sentEvents Set from localStorage for cross-page performance
    initializeSentEventsFromStorage() {
        if (!this.isLocalStorageAvailable()) return;
        
        try {
            const key = 'analytics_sent_events';
            const stored = localStorage.getItem(key);
            if (stored) {
                const sentEvents = JSON.parse(stored);
                // Initialize the Set with recent sent events for fast lookup
                this.sentEvents = new Set(sentEvents);
                console.log(`Loaded ${sentEvents.length} sent events from previous session`);
            }
        } catch (error) {
            console.error('Failed to initialize sentEvents from storage:', error);
            // Keep empty Set as fallback
            this.sentEvents = new Set();
        }
    }

    async init() {
        if (this.initialized || !this.hasConsent('analytics')) return;

        try {
            if (!window.aws_amplify) {
                throw new Error('AWS Amplify not loaded');
            }

            const { Amplify, Analytics, Auth, AWSKinesisFirehoseProvider } = window.aws_amplify;

            Analytics.addPluggable(new AWSKinesisFirehoseProvider());
            Amplify.configure(this.config);
            Analytics.configure({
                AWSKinesisFirehose: {
                    region: this.config.aws_project_region,
                    bufferSize: 1,
                    flushSize: 1,
                    flushInterval: 0,
                    resendLimit: 2,                    // Quick retries for unload
                    resendLimitExceeded: 'keep',       // Don't drop events
                    requestTimeout: 2000,              // 2 second timeout
                    retryDelayOnFailure: 300,          // Fast retry for unload
                    enabled: true
                }
            });

            this.generateSessionId();
            await this.getAmplifySessionId();

            // Initialize sentEvents from localStorage for cross-page duplicate detection
            this.initializeSentEventsFromStorage();

            // Send initial page load event
            const formatter = this.getEventFormatter();
            if (formatter) {
                this.sendEventReliably(formatter.pageView(document.referrer), true);
            }

            this.trackNavigation();
            this.trackClicks();
            this.trackScroll();
            this.setupUnloadHandling();
            
            // Retry any events that failed to send in previous sessions
            this.retryPendingEvents();
            
            // Set up periodic cleanup every 30 minutes
            this.setupPeriodicCleanup();

            this.initialized = true;
            console.log('Analytics initialized successfully');
        } catch (error) {
            console.error('Failed to initialize analytics:', error);
        }
    }

    hasConsent(type = '') {
        if (!this.isLocalStorageAvailable()) {
            console.warn('localStorage not available, assuming no consent');
            return false;
        }
        
        try {
            const consentKey = Object.keys(localStorage).find(key => key.endsWith('consent'));
            const consent = consentKey ? JSON.parse(localStorage.getItem(consentKey) || '{}') : {};
            return type ? consent[type] === true : Object.keys(consent).length > 0;
        } catch (error) {
            console.error('Error checking consent:', error);
            return false;
        }
    }
}

// Initialize analytics
const analytics = new AnalyticsTracker();

document.addEventListener('DOMContentLoaded', () => {
    if (analytics.hasConsent('analytics')) {
        analytics.init();
    }
});

document.addEventListener('consent', (e) => {
    if (analytics.hasConsent('analytics') && !analytics.initialized) {
        analytics.init();
    }
});

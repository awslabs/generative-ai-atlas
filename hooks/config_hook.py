# scripts/config_hook.py
import sys
from urllib.parse import urlparse

def on_config(config, **kwargs):
    # Check if we're running 'serve' command
    if 'serve' in sys.argv:
        # Development settings
        config['extra_javascript'] = []
        config['site_url'] = 'http://localhost:8000/generative-ai-atlas'
    
    # Extract base path from site_url and make it available throughout the site
    site_url = config.get('site_url', '')
    base_path = ''
    if site_url:
        parsed = urlparse(site_url)
        base_path = parsed.path.rstrip('/')
        
        # Replace placeholder in copyright with actual base path
        if 'copyright' in config:
            config['copyright'] = config['copyright'].replace('{{BASE_URL}}', base_path)
    
    # Add base_path to extra config so it's available in templates
    if 'extra' not in config:
        config['extra'] = {}
    config['extra']['base_path'] = base_path
    
    return config

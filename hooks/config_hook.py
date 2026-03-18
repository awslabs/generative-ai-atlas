# hooks/config_hook.py
import logging
import sys
from urllib.parse import urlparse


class _WeasyPrintAnchorFilter(logging.Filter):
    """Filter the one remaining weasyprint anchor warning.

    A single anchor ('cohere.embed-english-v3') contains a dot that
    weasyprint cannot resolve.  This is harmless.
    """

    def filter(self, record: logging.LogRecord) -> bool:
        return "No anchor" not in record.getMessage()


class _FontToolsNoiseFilter(logging.Filter):
    """Filter harmless fontTools warnings from bundled woff2 fonts."""

    _NOISE = ("extra bytes in post.stringData", "seems very low")

    def filter(self, record: logging.LogRecord) -> bool:
        msg = record.getMessage()
        return not any(n in msg for n in self._NOISE)


logging.getLogger("weasyprint").addFilter(_WeasyPrintAnchorFilter())
logging.getLogger("fontTools.ttLib.tables._p_o_s_t").addFilter(_FontToolsNoiseFilter())
logging.getLogger("fontTools.ttLib.tables._h_e_a_d").addFilter(_FontToolsNoiseFilter())


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

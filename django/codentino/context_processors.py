import os
from codentino.settings import DEBUG

def site_meta(request):
    data = {
        'SITE_BRAND_URL': os.environ.get("SITE_BRAND_URL"),
        'SITE_TITLE': os.environ.get('SITE_TITLE'),
        'SITE_DESC': os.environ.get('SITE_DESC'),
        'GA_MEASUREMENT_ID': os.environ.get('GA_MEASUREMENT_ID', None)
    }

    return data

def settings_context(request):
    settings = {
        'DEBUG': DEBUG,
    }

    return settings
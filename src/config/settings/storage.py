STATIC_URL = config['storage']['static_url']
MEDIA_URL = config['storage']['media_url']

MEDIA_ROOT = config['storage']['media_root']
STATIC_ROOT = config['storage']['static_root']

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

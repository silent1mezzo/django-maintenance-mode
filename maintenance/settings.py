from django.conf import settings

def get(key, default):
    return getattr(settings, key, default)

NOTIFICATION_TIME = get('MAINTENANCE_MODE_NOTIFICATION_TIME', 10)
EMAIL_USERS = get('MAINTENANCE_MODE_EMAIL_USERS', False)
SAFE_IP = get('MAINTENANCE_MODE_SAFE_IP', ('127.0.0.1',))
TEMPLATE = get('MAINTENANCE_MODE_TEMPLATE', 'maintenance/maintenance.html')

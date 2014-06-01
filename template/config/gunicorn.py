import os
import multiprocessing
from django.conf import settings

# Properties
daemon = True
workers = multiprocessing.cpu_count() * 2 + 1

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
if settings.DEBUG:
    bind = '127.0.0.1:8000'
else:
    ip = os.environ['OPENSHIFT_GEO_IP']
    port = os.environ['OPENSHIFT_GEO_PORT']
    bind = '{}:{}'.format(ip, port)

import os
import multiprocessing

# Properties
daemon = True
workers = multiprocessing.cpu_count() * 2 + 1

# Setup server
ip = os.environ['OPENSHIFT_GEO_IP']
port = os.environ['OPENSHIFT_GEO_PORT']
bind = '{}:{}'.format(ip, port)

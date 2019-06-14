import os

server_tier = os.environ.get('SERVER_TIER') or 'local'

DEBUG = True
Local = True
SERVER_NAME = '127.0.0.1:5000'

if server_tier in ['local']:
    DEBUG = True
    LOCAL = True
    SERVER_NAME = '127.0.0.1:5000'
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 5000
FLASK_DEBUG = False
FLASK_THREADED = True

import os
MONGO_DATABASE = os.environ['MONGO_DATABASE']
MONGO_ROOT_USERNAME = os.environ['MONGO_ROOT_USERNAME']
MONGO_ROOT_PASSWORD = os.environ['MONGO_ROOT_PASSWORD']
MONGO_API = 'mongodb://{}:{}@db:27017/{}'.format(MONGO_ROOT_USERNAME, MONGO_ROOT_PASSWORD, MONGO_DATABASE)

SALT = 'zmeflzejZEFIlqksjdAOQM3JQDJSJ82'

NEWSAPI_KEY = '3e2d2a5313cf4208a83cb8c65d1e9677'

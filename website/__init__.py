import os
import random
import string

from flask import Flask

_path = os.getcwd()
UPLOAD_FOLDER = os.path.join(_path, 'uploads')
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

def create_app():
    global UPLOAD_FOLDER
    _str_ = string.ascii_lowercase
    _secret_key_ = ''.join(random.choice(_str_) for i in range(12))

    app = Flask(__name__)
    app.config['SECRET KEY'] = _secret_key_
    app.secret_key = _secret_key_
    app.config['MAX_CONTENT_LENGTH'] = 100*1024*1024
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    from .auth import auth
    from .views import views

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    return app


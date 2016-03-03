import os
from os import path
from flask import Flask

from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import config
from flask.ext.uploads import patch_request_class


moment = Moment()


basedir = path.abspath(path.dirname(__file__))


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    basedir = path.abspath(path.dirname(__file__))

    MUSIC_FOLDER = os.path.join(basedir, 'static/musics')
    app.config['MUSIC_FOLDER'] = MUSIC_FOLDER

    moment.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app

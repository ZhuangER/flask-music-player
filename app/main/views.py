import os
from flask import render_template, request, flash, redirect, url_for, jsonify, make_response
from flask.ext.login import current_user, login_required
from werkzeug.utils import secure_filename
from . import main
from manage import app
from ..models import Photo
from .. import db



@main.route('/healthcheck')
def healthcheck():
    return "200"


@main.route('/')
@main.route('/index', methods=['GET', 'POST'])
def index():
    music_folder = app.config['MUSIC_FOLDER']
    music_list = os.listdir(music_folder)
    return render_template('music/index.html', music_list = music_list)
from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import current_user, login_required
from . import music
from .. import db
import manage
import os

@music.route('/index', methods=['GET', 'POST'])
@login_required
def index():
	if current_user.is_authenticated:
		music_folder = manage.app.config['MUSIC_FOLDER']
		music_list = os.listdir(music_folder)
	return render_template('music/index.html', music_list = music_list)
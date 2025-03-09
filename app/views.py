
"""

Contains routes for Flask application

"""

from flask import Blueprint, redirect, render_template, url_for

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return render_template('home.html')
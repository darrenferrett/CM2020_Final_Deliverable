
"""

Contains routes for Flask application

"""

from flask import Blueprint, render_template

base = Blueprint('base', __name__)

@base.route('/')
# ‘/’ URL is bound with hello_world() function.
def home():
    return render_template('home.html')

"""

Flask init file

"""

from flask import Flask
from app.views import home

def create_app():
    app = Flask(__name__)
     
    # Register the blueprint
    app.register_blueprint(home)
    
    return app
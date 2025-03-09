
"""

CM2020 Final Submission - Software Project

Student number: 

Gamevey - Gamified Survey Application

"""

from app import create_app
from flask_sqlalchemy import SQLAlchemy

    
# Create Flask application    
app = create_app()

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///gamevey.db"
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
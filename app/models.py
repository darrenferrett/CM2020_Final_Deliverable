
"""

Contains models for Flask application

"""

""" Surveys DB model """

class Surveys(db.model):
	""" Surveys """
	
	survey_name = db.column(db.String(32), nullable=False, primary_key=True)
	survey_description = db.column(db.String(256))
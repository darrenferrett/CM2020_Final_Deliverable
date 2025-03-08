
"""

CM2020 Final Submission - Software Project

Student number: 

Gamevey - Gamified Survey Application

"""

from flask import Flask

# Flask constructor
app = Flask(__name__)

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'


# main function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
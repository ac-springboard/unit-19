from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Survey, satisfaction_survey as satisfaction

# INITIALIZATION
app = Flask(__name__)
app.config['SECRET_KEY'] = 'password123'
debug = DebugToolbarExtension(app)

# GLOBAL VARIABLES
responses = list()
survey = Survey(satisfaction.title, satisfaction.instructions, satisfaction.questions)


# ROUTERSs
@app.route('/')
def root_viewS():
    return render_template('root.html',
                           survey_title=survey.title,
                           survey_instructions=survey.instructions,
                           page_title='Survey Home')

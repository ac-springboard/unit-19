from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Survey, satisfaction_survey as satisfaction

# INITIALIZATION
app = Flask(__name__)
app.config['SECRET_KEY'] = 'password123'
debug = DebugToolbarExtension(app)

# GLOBAL VARIABLES
responses = list()
survey = Survey(satisfaction.title, satisfaction.instructions, satisfaction.questions)


# ROUTERS
@app.route('/')
def root_view():
    return render_template('root.html',
                           survey_title=survey.title,
                           survey_instructions=survey.instructions,
                           page_title='Survey Home')


@app.route('/questions/<int:qn>')
def questions_view(qn):
    if qn >= len(survey.questions):
        return redirect('/thankyou')

    next_question = qn + 1
    return render_template('questions.html',
                           survey_title=survey.title,
                           question_statement=f"{qn}. {survey.questions[qn].question}",
                           question_choices=survey.questions[qn].choices,
                           next=next_question,
                           page_title=f"Question #{qn}")

from flask import Flask, request, render_template, redirect
#from flask_debugtoolbar import DebugToolbarExtension
from surveys import Survey, satisfaction_survey as satisfaction

# INITIALIZATION

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'password123'
#debug = DebugToolbarExtension(app)

# GLOBAL VARIABLES

responses = list()
survey = Survey(satisfaction.title, satisfaction.instructions, satisfaction.questions)
thankyou_statement = "Thank you!"


# ROUTES

@app.route('/')
def root_view():
    return render_template('root.html',
                           survey_title=survey.title,
                           survey_instructions=survey.instructions,
                           page_title='Survey Home')


@app.route('/questions/<int:question_number>')
def questions_view(question_number):
    if is_invalid_request(question_number):
        return redirect('/')

    return render_template('questions.html',
                           survey_title=survey.title,
                           question_statement=f"{question_number}. {survey.questions[question_number].question}",
                           question_choices=survey.questions[question_number].choices,
                           question_number=question_number,
                           page_title=f"Question #{question_number}")


@app.route("/answer/<int:question_number>", methods=['POST'])
def answer_service(question_number):
    if is_invalid_request(question_number):
        return redirect('/')

    try:
        if request.method == "GET":
            answer = request.args['answer']
        else:
            answer = request.form['answer']
        responses.append(answer)
    except Exception as e:
        print(e)
        redirect('/question/{question_number}')

    if is_last_question(question_number):
        return redirect('/thankyou')

    return redirect(f'/questions/{len(responses)}')

@app.route("/thankyou")
def thankyou_view():
    return render_template('thankyou.html', thankyou_statement = thankyou_statement )

# AUXILIARY FUNCTIONS

def is_last_question(question_number):
    return question_number == len(survey.questions) - 1


def is_invalid_request(question_number):
    return is_survey_closed() or is_invalid_question_number(question_number)


def is_survey_closed():
    return len(responses) == len(survey.questions)


def is_invalid_question_number(question_number):
    return question_number not in range(len(survey.questions)) or \
           question_number != len(responses)

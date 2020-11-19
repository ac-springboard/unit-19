from flask import Flask, request, render_template, redirect, flash
# from flask_debugtoolbar import DebugToolbarExtension
from surveys import Survey, satisfaction_survey as satisfaction

# INITIALIZATION

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password123'
# debug = DebugToolbarExtension(app)

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
                           page_label='root_page',
                           page_title='Survey Home')


@app.route('/questions/<int:question_number>')
def questions_view(question_number):
    if is_invalid_request(question_number):
        return redirect('/')

    if is_last_question(question_number):
        congrats = """
        Congratulations! You made it to the last question of this survey!
        When you answer to this question you will be automatically redirect to you Thank You page where a gift is waiting for you!
        """
    else:
        congrats = None
    return render_template('questions.html',
                           survey_title=survey.title,
                           question_statement=f"{question_number}. {survey.questions[question_number].question}",
                           question_choices=survey.questions[question_number].choices,
                           question_number=question_number,
                           top_message=congrats,
                           page_label='questions_page',
                           page_title=f"Question #{question_number}")


@app.route("/answer/<int:question_number>", methods=['GET'])
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
        flash('Something seems to be wrong. Have you answered the question?', ['questions_page', 'error'])
        flash("""If you have answered the question, 
        please contact Joe Biden and Kamala Harris
        at the White House on Jan 20, 2021 to file your complaint.""")
        return redirect(f'/questions/{question_number}')

    if is_last_question(question_number):
        return redirect('/thankyou')

    return redirect(f'/questions/{len(responses)}')


@app.route("/thankyou")
def thankyou_view():
    responses.clear();
    return render_template('thankyou.html',
                           thankyou_statement=thankyou_statement,
                           page_label='thankyou_page')


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

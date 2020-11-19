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
    responses.clear();
    return render_template('root.html',
                           survey_title=survey.title,
                           survey_instructions=survey.instructions,
                           page_label='root_page',
                           page_title='Survey Home')


@app.route('/questions')
def questions_view():
    if is_this_last_question():
        congrats = """
        Congratulations! You made it to the last question of this survey!
        When you answer to this question you will be automatically redirected to our Thank You page!
        """
    else:
        congrats = None

    question_number = get_this_question_number() - 1
    return render_template('questions.html',
                           survey_title=survey.title,
                           question_statement=f"{question_number + 1}. {survey.questions[question_number].question}",
                           question_choices=survey.questions[question_number].choices,
                           top_message=congrats,
                           page_label='questions_page',
                           page_title=f"Question #{question_number + 1}")


@app.route("/answer", methods=['GET'])
def answer_service():
    if is_invalid_request():
        return redirect('/')

    try:
        if request.method == "GET":
            answer = request.args['answer']
        else:
            answer = request.form['answer']
        responses.append(answer)
        print(answer)
        print(responses)
    except Exception as e:
        flash('Something seems to be wrong. Have you answered the question?', ['questions_page', 'error'])
        flash("""If you have answered the question, 
        please contact Joe Biden and Kamala Harris
        at the White House on Jan 20, 2021 to file your complaint.""")
        return redirect('/questions')

    if is_last_answered_question():
        return redirect('/thankyou')

    return redirect('/questions')


@app.route("/thankyou")
def thankyou_view():
    responses.clear()
    return render_template('thankyou.html',
                           survey_title=survey.title,
                           thankyou_statement=thankyou_statement,
                           page_label='thankyou_page')


# AUXILIARY FUNCTIONS

def is_last_answered_question():
    it_is = get_question_number() == len(survey.questions)
    return it_is


def is_invalid_request():
    return is_survey_closed()


def is_survey_closed():
    return len(responses) == len(survey.questions)


def get_question_number():
    return len(responses)


def is_this_last_question():
    it_is = get_this_question_number() == len(survey.questions)
    return it_is


def get_this_question_number():
    return get_question_number() + 1

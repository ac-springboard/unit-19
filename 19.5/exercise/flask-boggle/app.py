from flask import Flask, render_template, request
# from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password123'

# boggle_game = Boggle()

ncols = 4
nrows = 4


@app.route('/')
def root_view():
    return render_template('index.html')

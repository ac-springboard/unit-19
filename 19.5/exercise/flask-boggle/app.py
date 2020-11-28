from flask import Flask, render_template, request

# from math import floor, ceil

# from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password123'

# boggle_game = Boggle()

# Classes
ROW_CLASS = "row d-flex flex-nowrap justify-content-center"

# Fixed due my choice of the design
LATERAL_COL_WIDTH = 2
BOARD_MIN_LETTERS_PER_SIDE = 3
BOARD_MAX_LETTERS_PER_SIDE = 6
# <letters: cols>
BOARD_SIZE_PER_NUMBER_OF_LETTERS = {3: 6, 4: 4, 5: 5, 6: 6}

# Calculated Sizes
board_number_of_letters_per_side = 3
board_size = BOARD_SIZE_PER_NUMBER_OF_LETTERS.get(board_number_of_letters_per_side)
letter_cell_size = board_size / board_number_of_letters_per_side


@app.route('/')
def root_view():
    return render_template('index.html', square_width=board_size,
                           lateral_col_width=LATERAL_COL_WIDTH,
                           row_class=ROW_CLASS)

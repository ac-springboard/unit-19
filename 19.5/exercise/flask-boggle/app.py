from flask import Flask, render_template, request

# from math import floor, ceil

# from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password123'

# boggle_game = Boggle()

# Classes
ROW_CLASS = "row d-flex flex-nowrap justify-content-center"

# Fixed due my choice of the design
LATERAL_COL_WIDTH = 3
BOARD_MIN_LETTERS_PER_SIDE = 3
BOARD_MAX_LETTERS_PER_SIDE = 6
# <letters: cols>
BOARD_SIZE_PER_NUMBER_OF_LETTERS = {3: 6, 4: 4, 5: 5, 6: 6}

#
#

board_and_time = {
    '3x3': 45, '4x4': 60, '5x5': 75, '6x6': 90
}

# This is the variable that triggers layout
DEFAULT_NUMBER_OF_LETTERS_PER_SIDE = 4

# Calculated Values
default_grid = f'{DEFAULT_NUMBER_OF_LETTERS_PER_SIDE}x{DEFAULT_NUMBER_OF_LETTERS_PER_SIDE}'
default_time = board_and_time.get(default_grid)
board_number_of_letters_per_side = DEFAULT_NUMBER_OF_LETTERS_PER_SIDE
board_size_in_cols = BOARD_SIZE_PER_NUMBER_OF_LETTERS.get(board_number_of_letters_per_side)
letter_cell_size_in_cols = board_size_in_cols / board_number_of_letters_per_side


@app.route('/')
def root_view():
    return render_template('index.html', square_width=board_size_in_cols,
                           lateral_col_width=LATERAL_COL_WIDTH,
                           row_class=ROW_CLASS,
                           board_and_time=board_and_time,
                           default_grid=default_grid)

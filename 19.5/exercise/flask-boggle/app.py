from flask import Flask, render_template, request, jsonify

# from math import floor, ceil
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password123'

boggle_game = Boggle()

# Classes
ROW_CLASS = "row d-flex flex-nowrap justify-content-center"

# Fixed due my choice of the design
LATERAL_AREA_WIDTH_IN_COLS = 3
BOARD_MIN_chars_PER_SIDE = 3
BOARD_MAX_chars_PER_SIDE = 6
# <chars: cols>
BOARD_SIZE_IN_COLS_PER_GRID_SIZE = {'3x3': 6, '4x4': 4, '5x5': 5, '6x6': 6}
BOARD_AND_TIME = {'3x3': 45, '4x4': 60, '5x5': 75, '6x6': 90}

# This is the variable that triggers the layout
DEFAULT_GRID = '4x4'


# CONSONANT_LIST = list('bcdfghjklmnopqrstvwxyz')
# VOWEL_LIST=list('aeiou');


# Calculated Values
# board_number_of_chars_per_side = parseGrid( DEFAULT_GRID )
# board_size_in_cols = BOARD_SIZE_PER_GRID_SIZE.get(DEFAULT_NUMBER_OF_chars_PER_SIDE)
# char_cell_size_in_cols = board_size_in_cols / board_number_of_chars_per_side


# board=boggle_game.make_board();
@app.route('/')
def root_view():
    grid_size = request.args.get('grid_size', DEFAULT_GRID)
    print('grid_size', grid_size)
    board_size_in_cols = get_board_size_in_cols(grid_size)
    number_of_chars_per_side = get_number_of_chars_per_side(grid_size)
    char_cell_size_in_cols = get_char_cell_size_in_cols(board_size_in_cols, grid_size)
    # char_cell_size_in_pct = get_char_cell_size_in_pct(number_of_chars_per_side)
    board = make_empty_board(number_of_chars_per_side)
    return render_template('index.html', board_size_in_cols=board_size_in_cols,
                           number_of_chars_per_side=number_of_chars_per_side,
                           char_cell_size_in_cols=char_cell_size_in_cols,
                           # char_cell_size_in_pct=char_cell_size_in_pct,
                           lateral_area_width_in_cols=LATERAL_AREA_WIDTH_IN_COLS,
                           row_class=ROW_CLASS,
                           board_and_time=BOARD_AND_TIME,
                           grid_size=grid_size,
                           board=board,
                           initial_time=BOARD_AND_TIME.get(grid_size))


@app.route('/chars/<int:number_of_chars_per_side>')
def make_board_ajax(number_of_chars_per_side):
    if number_of_chars_per_side == 0:
        board = make_empty_board(number_of_chars_per_side)
    else:
        board = boggle_game.make_board(number_of_chars_per_side)
    return render_template('board.html', board=board,
                           number_of_chars_per_side=number_of_chars_per_side)


def make_empty_board(number_of_chars_per_side):
    board = [['🦉'] * (number_of_chars_per_side)] * number_of_chars_per_side
    return board


# def setup_variables( grid_size ):
def get_board_size_in_cols(grid_size):
    board_size = BOARD_SIZE_IN_COLS_PER_GRID_SIZE.get(grid_size)
    return board_size


def get_char_cell_size_in_cols(board_size_in_cols, grid_size):
    number_of_chars_per_side = get_number_of_chars_per_side(grid_size)
    char_cell_size_in_cols = int(board_size_in_cols / number_of_chars_per_side)
    return char_cell_size_in_cols


# def get_char_cell_size_in_pct():
#     return 25


def get_number_of_chars_per_side(grid_size):
    chars_per_side = grid_size.split('x')
    print(chars_per_side)
    return int(chars_per_side[0])

# def get_random_chars(n):
#     vowel = sample(VOWEL_LIST, )
#     cons = sample(CONSONANT_LIST, n-2)

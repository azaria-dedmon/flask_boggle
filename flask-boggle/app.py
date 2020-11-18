from flask import Flask, request, render_template, redirect, flash, jsonify
from flask import session
from boggle import Boggle
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenzarecool"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def create_board():
    board = boggle_game.make_board()
    session['board'] = board

    return render_template('board.html', board=board)

@app.route('/check-answer')
def check_answer():
    word = request.args["word"]
    return word
from flask import Flask, request, render_template, g, current_app
from database import queryDatabase, importDatabase
from board import cb, individualBoardPostData

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    board = queryDatabase('SELECT * FROM board ORDER BY board_name')
    board1, board2, board3 = [], [], []
    sz = len(board)
    for i in range(0, sz):
        if i < sz//3:
            board1.append(board[i])
        elif i >= sz//3 and i < (2*(sz//3)):
            board2.append(board[i])
        else:
            board3.append(board[i])
    return render_template('index.html', board = board, board1 = board1, board2 = board2, board3 = board3)

@app.route('/createBoard/', methods = ['GET', 'POST'])
def createBoard():
    return cb()

@app.route('/b/<board>')
def showBoard(board):
    return individualBoardPostData(board)

if __name__== "__main__":
    app.run(debug=True)

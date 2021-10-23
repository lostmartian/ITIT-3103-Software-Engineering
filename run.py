from flask import Flask, request, render_template, g, current_app
from database import queryDatabase, importDatabase
from board import cb

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    board = queryDatabase('SELECT * FROM board')
    return render_template('index.html', board = board)

@app.route('/createBoard/', methods = ['GET', 'POST'])
def createBoard():
    return cb()

if __name__== "__main__":
    app.run(debug=True)

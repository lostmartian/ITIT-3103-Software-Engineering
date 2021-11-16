from flask import request, render_template
from database import importDatabase, queryDatabase
from flask.helpers import flash, url_for
from werkzeug.utils import redirect


def generateBoard():
    if request.method == 'GET':
        return render_template('createBoard.html')
    else:
        db = importDatabase()
        name = request.form['board_name']
        description = request.form['board_description']

        error = None

        if not name:
            error = 'Board name not present'
        elif not description:
            error = 'Board description not present'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO board (board_name, board_description) VALUES (?,?)", (name, description), )
                db.commit()
            except db.IntegrityError:
                error = f"Board {name} is already present"
            else:
                return redirect(url_for('index'))

        flash(error)

def cb():
    rv = generateBoard()
    return rv

def deleteBoard(board_name):
    db = importDatabase()

def boardShow(boardname):
    posts = queryDatabase('SELECT * FROM posts WHERE board = "{}"'.format(boardname))
    return posts

def individualBoardPostData(board):
    posts = boardShow(board)
    boarddescription = queryDatabase(
        'SELECT board_description FROM board WHERE board_name = "{}"'.format(board))
    return render_template('boardDisplay.html', posts = posts, board=board, boarddescription=boarddescription)

    

from re import L
from flask import request, render_template
from database import queryDatabase

def newBoard():
    if request.method == 'GET':
        return render_template('newboard.html')
    else:
        if request.form.get('post_text'):
            if 'board_name' in request.files:
                name = request.files['board_name']
            if 'board_description' in request.files:
                description = request.files['board_description']
            return queryDatabase("INSERT INTO board (board_name, board_description) VALUES (?, ?)", (name, description))

def createBoard():
    return newBoard
import random
import os
import datetime
from flask import request, render_template
from database import importDatabase, queryDatabase
from flask.helpers import flash, url_for
from werkzeug.utils import redirect, secure_filename


allowed_extensions = set(['jpg', 'jpeg', 'png', 'gif'])


class postRequests:
    def __init__(self, board, app):
        self.board = board
        self.app = app
        
    def validFileName(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

    def postAddDB(self, request, reply_id):
        error = None
        if reply_id == '0':
            query = ''' INSERT INTO posts(image_, user, posted_on, board, post_text) VALUES (?,?,?,?,?) '''
        else:
            query = ''' INSERT INTO replies(image_, user, posted_on, board, post_text, replying_to) VALUES (?,?,?,?,?,?) '''
        db = importDatabase()
        try:
            db.execute(query, request)
            db.commit()
            print("Committed")
        except db.IntegrityError:
            error = f"Integrity error"
        else:
            return redirect(url_for('showBoard', board=self.board))


    def postCreation(self):
        filename = ''
        if request.form.get('post_text'):
            if 'image' in request.files:
                file = request.files['image']
                if file and self.validFileName(file.filename):
                    print("Correct File")
                    filename = secure_filename(file.filename)
                    newfilename = str(random.randint(1000000, 100000000))+'.'+filename.rsplit('.', 1)[1].lower()
                    file.save(os.path.join(self.app.config['upload_folder'], newfilename))
            now = datetime.datetime.now()
            post = (newfilename, request.form.get('user'),
                now.isoformat(), self.board, request.form.get('post_text'))
            print(self.postAddDB(post, '0'))
        return 'posted'

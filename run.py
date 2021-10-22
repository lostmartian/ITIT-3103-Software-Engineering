from flask import Flask, request, render_template
from database import importDatabase, queryDatabase

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    get_boards = queryDatabase('SELECT * FROM board')
    return render_template('index.html', boards = get_boards)



if __name__== "__main__":
    app.run(debug=True)
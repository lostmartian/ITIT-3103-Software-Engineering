from flask import Flask, request, g, render_template

app = Flask(__name__, static_url_path='/static')

def import_database():
    db = getattr(g, '_database', None)

@app.route('/')
def hello():
    return "Hello"

if __name__== "__main__":
    app.run(debug=True)
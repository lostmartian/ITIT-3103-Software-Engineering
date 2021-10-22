from flask import g, Flask
import sqlite3

from flask.helpers import get_flashed_messages

def importDatabase():
    if 'db' not in g:
        g.db = sqlite3.connect('datavase.db')
    return g.db

def queryDatabase(query, args=()):
    get_query = importDatabase().execute(query, args).fetchall()
    return get_query


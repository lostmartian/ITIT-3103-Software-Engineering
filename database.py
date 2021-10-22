from flask import g
import sqlite3

def importDatabase():
    if 'db' not in g:
        g.db = sqlite3.connect('database.db')
    return g.db

def queryDatabase(query, args=()):
    get_query = importDatabase().execute(query, args).fetchall()
    return get_query


from flask import g
import sqlite3

def importDatabase():
    db = db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('database.db')

def queryDatabase(query, args=(), ):


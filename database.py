from flask import g
import sqlite3

def importDatabase():
    db = getattr(g, '_database', None)

    if db is None:
        db = g._database = sqlite3.connect('database.db')

    return db
    
def queryDatabase(query, args=()):
    get_query = importDatabase().execute(query, args)
    rv = get_query.fetchall()
    return rv


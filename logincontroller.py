# This file controls the users login and authentication and reads the users data from the main database projdata.db


import sqlite3 as sql
from flask import session 
#adding users
def insertUser(username,email,psw,fbid):
    con = sql.connect("projdata.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,email,password,id) VALUES (?,?,?,?)", (username,email,psw,fbid))
    cur.execute("SELECT  *  from users")
    print(cur.fetchall())
    con.commit()
    con.close()


def retrieveUsers():
	con = sql.connect("projdata.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM users")
	users = cur.fetchall()
	con.close()
	return users

# for fb login
def checkUsers(name):
    con = sql.connect("projdata.db")
    con.row_factory = sql.Row
    db = con.cursor()
	
    userlist = db.execute("SELECT * from users where username = '%s'" %name)
    userexists = userlist.fetchall()
    if userexists:
        print("user exists")
        return True
    else:
        return False

    
# for normal login
def verifyUsers(username, password):
    con = sql.connect('projdata.db')
    con.row_factory = sql.Row
    db = con.cursor()
	
    userlist = db.execute("SELECT * from users where username = '%s'" %username)
    userexists = userlist.fetchall()
    if userexists:
        c = db.execute("SELECT * from users where password = '%s'" %password)
        passwcorrect = c.fetchall()
        if passwcorrect:
            session['username'] = username
            session['logged_in'] = True
            return True
        else:
            return False
    else:
        return False

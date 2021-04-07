# This file adds/remove/gets/deletes user favourites to the favourites table in main database projdata.db


import sqlite3
import favoriteController


def addtoDB(username, title, url, userTitle):
    conn = sqlite3.connect('projdata.db')
    c = conn.cursor()
    c.execute("INSERT INTO favourites (username,Title,link, userTitle) VALUES (?,?,?,?)" ,(username, title, url,userTitle))
    conn.commit()
    conn.close()

def removefromDB(userTitle):
    conn = sqlite3.connect('projdata.db')
    c = conn.cursor()
    c.execute("DELETE FROM favourites  where userTitle = '%s' " %userTitle)
    conn.commit()
    conn.close()

def getFav(username):
    conn = sqlite3.connect('projdata.db')
    c = conn.cursor()
    c.execute("SELECT * FROM favourites where username = '%s' " %username)
    result = c.fetchall()
    return result


def deletefav(username, keywordDelete):
    for w in favoriteController.favoriteKeywordList:
        if keywordDelete == w:
            v = favoriteController.favoriteKeywordList.index(w)
    favoriteController.favoriteList.pop(v)
    favoriteController.favoriteKeywordList.pop(v)
    removefromDB(username+keywordDelete)


#createTable()
#result = getFav("test")
#print(result)
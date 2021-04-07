# This file reads the popular courses data from the main database projdata.db

import sqlite3

## Function to get top 10 popular courses
def popcourses():
    con = sqlite3.connect('projdata.db')
    con.row_factory = sqlite3.Row
    db = con.cursor()
    getpackages = db.execute("SELECT * FROM salarydata ORDER BY Salary DESC LIMIT 10 ")
    items = getpackages.fetchall()
    return items

## Function to get all popular courses
def allpopcourses():
    con = sqlite3.connect('projdata.db')
    con.row_factory = sqlite3.Row
    db = con.cursor()
    getcourses = db.execute("SELECT * FROM salarydata ORDER BY Salary DESC")
    items = getcourses.fetchall()
    return items

#items = popcourses().fetchall()
#print(items)
#i=0
#for i in items:
    #print(i['University'])

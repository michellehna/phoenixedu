# This file reads the careerdata from the main database projdata.db

import sqlite3

def career():
    con = sqlite3.connect ('projdata.db')
    con.row_factory = sqlite3.Row
    db = con.cursor()
    getpackages = db.execute("SELECT rowid, * FROM careerfield")
    items = getpackages.fetchall()
    return items

def selectedcareer(shortform):
    con = sqlite3.connect ('projdata.db')
    con.row_factory = sqlite3.Row
    db = con.cursor()
    querystring= "SELECT DISTINCT field FROM careerfield where alias = '" +shortform + "'"
    getpackages = db.execute(querystring)
    items = getpackages.fetchall()
    return items


#mylist = career()
#print(items)#
#i=0

##result = selectedcareer('BnBS')
#print(result)
#for i in result:
   #print(i['field'])    
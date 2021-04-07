# This file reads the category data from the main database projdata.db


import sqlite3 as sql


def getCatlist(keyword):
    con = sql.connect("projdata.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM cat where Category = '%s'" %keyword)
    return cur.fetchall()


#result= getCatlist('Arch')

#for i in result:
    #print(i[3])
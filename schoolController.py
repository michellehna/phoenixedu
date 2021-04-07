# This controllers gets the poly list and uni list 


#import requests
import sqlite3

poly= {
    "TemasekPoly": ["Temasek Polytechnic","5d4a3afd-0ff6-4f90-833e-8b48587a0c72","static/images/Temasek.png","TemasekPoly"],
    "RepublicPoly": ["Republic Polytechnic","b44bd1e0-c37f-415f-b362-01ea4af577e9","static/images/Republic.jpg","RepublicPoly"],
    "NgeannPoly": ["Ngee Ann Polytechnic","4c2c13d7-655d-4344-b2f9-4327f6bcd662","static/images/Ngeeann.jpg","NgeannPoly"],
    "SingaporePoly": ["Singapore Polytechnic","b07ed06c-f67a-4bf3-a18a-0e0bf71e8f1a","static/images/Singapore.jpg","SingaporePoly"],
    "NanyangPoly": ["Nanyang Polytechnic","9d604589-a4ba-48ac-a792-560177c30332&q=2019","static/images/Nanyang.png","NanyangPoly"]
    }


def unilist():
    con = sqlite3.connect ('projdata.db')
    con.row_factory = sqlite3.Row
    db = con.cursor()
    getpackages = db.execute("SELECT DISTINCT university, logo FROM institution")
    items = getpackages.fetchall()
    return items

###unidata= unilist()

#for i in unidata:
   # print(i['university'])
   # print(i['logo'])
    #print(i['link'])
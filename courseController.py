# This file calls the data.gov.sg API to get the poly courses list data and the university courses list data from projdata.db main database.


import sqlite3
import requests
import schoolController

def polycourselist(polyname):
    sname= polyname
    resource = schoolController.poly[sname][1]
    response = requests.get('https://data.gov.sg/api/action/datastore_search?resource_id='+ resource)
    json_response = response.json()
    alldata =json_response["result"]["records"]
    return alldata

def unicourselist(uniname):
    con = sqlite3.connect ('projdata.db')
    con.row_factory = sqlite3.Row
    db = con.cursor()
    querystring= "SELECT Course, CourseLink FROM institution where University = '" +uniname +"'"
    getpackages = db.execute(querystring)
    items = getpackages.fetchall()
    return items


#unicoursedata=unicourselist('NTU')   

#for i in unicoursedata:
   # print(i['Course'])
   # print(i['CourseLink'])

#polycoursedata=polycourselist('TemasekPoly')

#for i in polycoursedata:
   # print(i['course_name'])
   # print(i['reference'])
    #print(i)

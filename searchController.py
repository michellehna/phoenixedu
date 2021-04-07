# This controller gets the search keyword and provide relevant result



import schoolController
import categoryController
import categoryEntity
import pandas
import sqlite3
##keyword = ("Temasek").lower()

i=0
j=0
#print("Schools are:")
polylist= schoolController.poly
unilist = schoolController.unilist()
#print(schoollist)
#for i in schoollist:
    #if keyword in schoollist[i][0].lower():   
       # print(schoollist[i])
    #else:
       # print("No results found")

#print("Categories are:")
categorylist= list(categoryEntity.courses_by_key.keys())
#print(categorylist)
#if keyword in categorylist:
   # filename = (keyword+'.csv')
   # data = pandas.read_csv(filename, header=0)
   # category = list(data.values)
    #print(category)

    #for value in category:
       # print(value[0])
       # print(value[2])
#
       ## print(value[0] + '   ' + value[2])
#print("starting function \n")
#key=("Temasek").lower()

def searchinst(keyvalue):
    instdata=[]
    uni=[]
    #result= dict()
    #result['instdata']=[]
    #result['catdata']=""
    for i in polylist:
        if keyvalue.lower() in polylist[i][0].lower():
            instdata.append(polylist[i])   
            #print(instdata)
        #result['catdata']= category
        #print(category)
    #for j in unilist:
    return (instdata)



#print(searchinst('n'))

#def unilist():
   # con = sqlite3.connect ('projdata.db')
   # con.row_factory = sqlite3.Row
   # db = con.cursor()
   # getpackages = db.execute("SELECT DISTINCT university, logo FROM institution")
    #items = getpackages.fetchall()
    #return items


#c.execute('''CREATE TABLE cat (Category text,Schools text,Type text,URL text,Logo text)''')

#categorylist= list(categoryEntity.courses_by_key.keys())
def searchcat(keyvalue):
    catdata=[]
    if keyvalue in categorylist:
        #filename = (keyvalue+'.csv')
        #data = pandas.read_csv(filename, header=0)
        #catdata = list(data.values)
        catdata=categoryController.getCatlist(keyvalue)
    return (catdata)    

#print("starting function \n")

#print(searchinst(key))
#instlist=searchcat('Arch')
#print(instlist)
#for value in instlist:
      #print(value[1])
      ##print(value[2])
     #   print(value[0] + '   ' + value[2])
#print("end function \n")


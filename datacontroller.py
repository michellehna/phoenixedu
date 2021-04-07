# This file creates the main database projdata.db


import sqlite3
import pandas as pd

conn = sqlite3.connect('projdata.db')
c = conn.cursor()

#creating table for uni data with salary for popular courses
c.execute('''CREATE TABLE salarydata (Programme text,University text,Test int,Salary int, Link text, Image text)''')
uni = pd.read_csv('CSV/testdata.csv')
uni.to_sql('salarydata', conn, if_exists='append', index = False)

print(c.execute('''SELECT * FROM salarydata''').fetchall())

print()

#creating table for all category
c.execute('''CREATE TABLE cat (Category text,Schools text,Type text,URL text,Logo text)''')
cat = pd.read_csv('CSV/cat.csv')
cat.to_sql('cat', conn, if_exists='append', index = False)

print(c.execute('''SELECT * FROM cat''').fetchall())

print()


#creating table for career
c.execute ('''CREATE TABLE careerfield (alias text,field text,Agriculture text,Architecture text,BnBS text,Business text,CnJ text,CS text,CAnPS text,Education text,Engineering text,Legal text,LAnH text,MnRT text,MnHP text,PS text,Psychology text,TnD text,VnPA text,Other text)''')
career = pd.read_csv('CSV/CareerData.csv')
career.to_sql('careerfield', conn, if_exists='append', index = False)
print(c.execute('''SELECT * FROM careerfield''').fetchall())
print()

#creating table for institutions
c.execute ('''CREATE TABLE institution (University text,Course text,CourseLink text,Logo text)''')
institution = pd.read_csv('CSV/Uni_Course_Data.csv')
institution.to_sql('institution', conn, if_exists='append', index = False)
print(c.execute('''SELECT * FROM institution''').fetchall())


#creating table for favourites
c.execute ('''CREATE TABLE favourites (username text,Title text,link text, userTitle  text)''')
print(c.execute('''SELECT * FROM favourites''').fetchall())

#creating table for user profile
c.execute('''Create TABLE users (username text not null,email text not null, password text not null,id text not null)''')
print(c.execute('''SELECT * FROM favourites''').fetchall())
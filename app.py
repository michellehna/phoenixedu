
## This is main boundary class to launch the application


## importing flask modules and other packages
from flask import Flask, render_template, redirect , url_for , request, abort , session, flash
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook
from flask_login import logout_user
import os
import sys
import requests
import sqlite3
import pandas

##importing controller files
import logincontroller as lg
import schoolController
import courseController
import rankingController
import categoryEntity
import categoryController
import searchController
import favoriteController
import FavController as fav
import popularcourseController
import careerController

 

#FLASK STUFF
app = Flask(__name__)

##Facebook API

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
app = Flask(__name__)
app.config["FACEBOOK_OAUTH_CLIENT_ID"] = '4191539264212565'
app.config["FACEBOOK_OAUTH_CLIENT_SECRET"] = '600c569ba77ad717df69a0e2761e2735'
facebook_bp = make_facebook_blueprint()
app.register_blueprint(facebook_bp, url_prefix="/login")
app.secret_key = 'hello'

#intialise null username
username=''


#Favourites list
favoriteRecord = fav.getFav(username)
for x in favoriteRecord:
    dict_fav = {}
    dict_fav["title"] = x[1]
    dict_fav["link"]  = x[2]
    favoriteController.favoriteList.append(dict_fav)
    favoriteController.favoriteKeywordList.append(dict_fav["title"])


#m(first page)- LOGIN PAGE
@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if request.form['submit_button'] == 'Login with Facebook':
            return redirect(url_for('fblogin'))
        
        else:
            session.permanent = True
            user = request.form["nm"]
            password = request.form["psw"]
            
            #print(user)
            if lg.verifyUsers(user, password) == True:
                return redirect(url_for('home'))
            else:
                return render_template("main.html", message = "Invalid username or password!")
            return render_template('main.html')
    else:
        return render_template("main.html")


##HOMEPAGE
@app.route('/home' , methods=['GET', 'POST'])
def home():
    popcourses = popularcourseController.popcourses()
    career = careerController.career()
    if request.method == 'POST':
        try:
            keyword = request.form['favorite']
            duplicate = 0
            dict_fav = {}
            z = keyword.split("#")
            dict_fav["title"] = z[1]
            dict_fav["link"]  = z[0]
            for x in favoriteController.favoriteKeywordList:
                if dict_fav["title"] == x:
                    duplicate = 1
            if duplicate == 0:
                favoriteController.favoriteList.append(dict_fav)
                favoriteController.favoriteKeywordList.append(dict_fav["title"])
                fav.addtoDB(username, dict_fav["title"], dict_fav["link"], username+dict_fav["title"])
        except: 
            pass
    if request.method == 'POST':
        try:
            keywordDelete = request.form['delete']
            fav.deletefav(username, keywordDelete)
        except:
            pass
    return render_template('index.html', popcourses=popcourses, career = career , favoriteList = favoriteController.favoriteList)

##INSITUTION LIST PAGE
@app.route('/schools', methods=['GET', 'POST'])
def schools():
    unidata= schoolController.unilist
    if request.method == 'POST':
        try:
            keywordDelete = request.form['delete']
            fav.deletefav(username, keywordDelete)
        except:
            pass
    return render_template('schoollist.html', sdata = schoolController.poly , unidata= unidata, i=0, favoriteList = favoriteController.favoriteList) 

##COURSE LIST PAGE
@app.route('/schools/<schoolname>' , methods=["POST", "GET"])   
def schoolname(schoolname):
    if schoolname in schoolController.poly.keys():
        courselist= courseController.polycourselist(schoolname)
        polyname= schoolController.poly[schoolname][0]
        if request.method == 'POST':
            try:
                keyword = request.form['favorite']
                duplicate = 0
                if keyword in favoriteController.favoriteSchoolChecklist:
                    dict_fav = {}
                    if keyword == "TemasekPoly":
                        dict_fav["title"] = "Temasek Polytechnic"
                    elif keyword == "RepublicPoly":
                        dict_fav["title"] = "Republic Polytechnic"
                    elif keyword == "NgeannPoly":
                        dict_fav["title"] = "Ngee Ann Polytechnic"
                    elif keyword == "SingaporePoly":
                        dict_fav["title"] = "Singapore Polytechnic"
                    elif keyword == "NanyangPoly" :
                        dict_fav["title"] = "Nanyang Polytechnic"
                    dict_fav["link"]  = "http://localhost:5000/schools/"+keyword
                    for x in favoriteController.favoriteKeywordList:
                        if dict_fav["title"] == x:
                            duplicate = 1
                    if duplicate == 0:
                        favoriteController.favoriteList.append(dict_fav)
                        favoriteController.favoriteKeywordList.append(dict_fav["title"])
                        fav.addtoDB(username, dict_fav["title"], dict_fav["link"], username+dict_fav["title"])
                else:
                    dict_fav = {}
                    y = keyword.split("#")
                    dict_fav["title"] = y[1]
                    dict_fav["link"]  = y[0]
                    for x in favoriteController.favoriteKeywordList:
                        if dict_fav["title"] == x:
                            duplicate = 1
                    if duplicate == 0:
                        favoriteController.favoriteList.append(dict_fav)
                        favoriteController.favoriteKeywordList.append(dict_fav["title"])
                        fav.addtoDB(username, dict_fav["title"], dict_fav["link"], username+dict_fav["title"])
            except:
                pass

        if request.method == 'POST':
            try:
                keywordDelete = request.form['delete']
                fav.deletefav(username, keywordDelete)
            except:
                pass
        return render_template('polycourselist.html', courselist =courselist, schoolname = polyname, schname = schoolname, favoriteList = favoriteController.favoriteList)


    else:   
        courselist= courseController.unicourselist(schoolname)
        uniname= schoolname
        try:
            keyword = request.form['favorite']
            duplicate = 0
            dict_fav = {}
            y = keyword.split("#")
            dict_fav["title"] = y[1]
            dict_fav["link"]  = y[0]
            for x in favoriteController.favoriteKeywordList:
                if dict_fav["title"] == x:
                    duplicate = 1
            if duplicate == 0:
                favoriteController.favoriteList.append(dict_fav)
                favoriteController.favoriteKeywordList.append(dict_fav["title"])
                fav.addtoDB(username, dict_fav["title"], dict_fav["link"], username+dict_fav["title"])
        except:
            pass

        if request.method == 'POST':
            try:
                keywordDelete = request.form['delete']
                fav.deletefav(username, keywordDelete)
            except:
                pass

        return render_template('unicourselist.html', courselist =courselist, schoolname = uniname, favoriteList = favoriteController.favoriteList)


##POPULARCOURSES PAGE
@app.route("/popularcourses", methods=['GET', 'POST'])
def popularcourses():
    allpopcourses= popularcourseController.allpopcourses()
    if request.method == 'POST':
        try:
            keyword = request.form['favorite']
            duplicate = 0
            dict_fav = {}
            z = keyword.split("#")
            dict_fav["title"] = z[1]
            dict_fav["link"]  = z[0]
            for x in favoriteController.favoriteKeywordList:
                if dict_fav["title"] == x:
                    duplicate = 1
            if duplicate == 0:
                favoriteController.favoriteList.append(dict_fav)
                favoriteController.favoriteKeywordList.append(dict_fav["title"])
                fav.addtoDB(username, dict_fav["title"], dict_fav["link"], username+dict_fav["title"])
        except:
            pass
    
    if request.method == 'POST':
        try:
            keywordDelete = request.form['delete']
            fav.deletefav(username, keywordDelete)
        except:
            pass
    return render_template("popularcourses.html", allpopcourses = allpopcourses, favoriteList = favoriteController.favoriteList)


## RANKING PAGE 
@app.route("/ranking", methods=['GET', 'POST'])
def ranking():
    if request.method == 'POST':
        try:
            keywordDelete = request.form['delete']
            fav.deletefav(username, keywordDelete)
        except:
            pass
    return render_template('ranking.html', title='Ranking', listofschools = rankingController.listofschools, favoriteList = favoriteController.favoriteList)


@app.route("/category", methods=['GET', 'POST'])
def category():
    if request.method == 'POST':
        try:
            keywordDelete = request.form['delete']
            fav.deletefav(username, keywordDelete)
        except:
            pass
    return render_template('category.html', courses=categoryEntity.courses, favoriteList = favoriteController.favoriteList) 

@app.route("/<categoryschool>", methods=['GET', 'POST'])
def show_course(categoryschool):
    
    categorycourse = categoryEntity.courses_by_key.get(categoryschool)
    categorydata = categoryController.getCatlist(categoryschool)
    if request.method == 'POST':
        try:
            keyword = request.form['favorite']
            duplicate = 0
            dict_fav = {}
            z = keyword.split("#")
            dict_fav["title"] = z[1]
            dict_fav["link"]  = z[0]
            for x in favoriteController.favoriteKeywordList:
                if dict_fav["title"] == x:
                    duplicate = 1
            if duplicate == 0:
                favoriteController.favoriteList.append(dict_fav)
                favoriteController.favoriteKeywordList.append(dict_fav["title"])
                fav.addtoDB(username, dict_fav["title"], dict_fav["link"], username+dict_fav["title"])
        except:
            pass
        
    if request.method == 'POST':
        try:
            keywordDelete = request.form['delete']
            fav.deletefav(username, keywordDelete)
        except:
            pass
    return render_template("categorycourses.html", categorydata = categorydata, favoriteList = favoriteController.favoriteList, csname = categoryschool , catcourse =categorycourse) 

##CAREER PAGE
@app.route('/home/<shortform>' , methods=["POST", "GET"])   
def shortform(shortform):
    
    career= careerController.career()
    selectedcareer = careerController.selectedcareer(shortform)
    if request.method == 'POST':
        try:
            keywordDelete = request.form['delete']
            fav.deletefav(username, keywordDelete)
        except:
            pass
    
    return render_template("Careerlist.html", career = career, shortform = shortform, selectedcareer = selectedcareer, favoriteList = favoriteController.favoriteList)


## SEARCH RESULT PAGE
@app.route('/searchresult' , methods=["POST", "GET"])
def searchresult():
    if request.method == 'GET':
        key=request.args.get("keyword")
        instdata= searchController.searchinst(key)
        catdata= searchController.searchcat(key)
        return render_template("searchresult.html", instdata = instdata, catdata = catdata, i=0, keyword=key)


# SIGNUP PAGE - register the new users
@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        email = request.form["email"]
        password = request.form["psw"]
        lg.insertUser(user, email, password, "-")
        flash("Registered successfully")
        session["user"] = user
        return redirect(url_for('index'))
    else:
        return render_template("signup.html")



#FACEBOOK LOGIN function
@app.route("/fblogin")
def fblogin():
    if not facebook.authorized:
        return redirect(url_for("facebook.login"))
    resp = facebook.get("/me")
    assert resp.ok, resp.text
    name = resp.json()["name"]
    username=name
    print(resp.json())
    fbid = resp.json()["id"]
    if lg.checkUsers(name):
        print("logged in")
    else: 
        lg.insertUser(name,"- ","-",fbid)

    return redirect(url_for('home'))


#LOGOUT the user
@app.route("/logout")
def logout():
    session.pop("user", None)
    username =""
    facebook.logout()
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)


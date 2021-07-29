# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getClothingWomenDetails, getClothingWomen1, getClothingWomen2,getClothingWomen3, getClothingMen1, getClothingMen2,getClothingMen3 
import os

# -- Initialization section --
app = Flask(__name__)



# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    details = getClothingWomenDetails()
    # urllist = getClothingUrl()
    # print(urllist)
    return render_template("index.html", time = datetime.now(), details =details)

@app.route('/men')
def men():
    
    return render_template("men.html")

# @app.route('/women')
# def women():
#     details = getClothingWomenDetails()
#     return render_template("women.html", details =details)

@app.route('/women$')
def women1():
    details = getClothingWomen1()
    return render_template("women$.html", details =details)

@app.route('/women$$')
def women2():
    details = getClothingWomen2()
    return render_template("women$$.html", details =details)

@app.route('/women$$$')
def women3():
    details = getClothingWomen3()
    return render_template("women$$$.html", details =details)

@app.route('/men$')
def men1():
    details = getClothingMen1()
    return render_template("men$.html", details =details)

@app.route('/men$$')
def men2():
    details = getClothingMen2()
    return render_template("men$$.html", details =details)

@app.route('/men$$$')
def men3():
    details = getClothingMen3()
    return render_template("men$$$.html", details =details)
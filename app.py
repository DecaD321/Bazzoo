# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getClothingPrices, getClothingUrl
import os

# -- Initialization section --
app = Flask(__name__)



# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    price = getClothingPrices()
    urllist = getClothingUrl()
    print(urllist)
    return render_template("index.html", time = datetime.now(), price = price, urllist = urllist)
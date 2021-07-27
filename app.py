# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getClothingPrices
import os

# -- Initialization section --
app = Flask(__name__)



# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    getClothingPrices()
    return render_template("index.html", time = datetime.now())


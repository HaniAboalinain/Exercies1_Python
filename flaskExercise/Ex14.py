# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 08:24:55 2019

@author: Hani
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "This is Index page"

@app.route('/hello')
def hello():
    return "Hello World"


@app.route('/members')
def mambers():
    return "Members Page"

@app.route('/index/<int:score>')
def isPassed(score):
    return render_template("hello.html" , score = score)

@app.route('/coding')
def css():
    return render_template("hello.html")


app.run()
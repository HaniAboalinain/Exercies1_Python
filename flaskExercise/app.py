# -*- coding: utf-8 -*-
"""
Created on Mon Dec  11 08:23:32 2019

@author: Hani
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hello/<int:score>')
def hello_world(score):
    return render_template("hello.html" , marks = score)


if __name__ == "__main__":
    app.run()

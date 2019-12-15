# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 2:55:00 2019

@author: Hani
"""


from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql
# Exercise 1
app = Flask(__name__)
@app.route("/")
def index():
   return render_template("login.html")

@app.route("/logedin/<name>/<int:age>/<address>/<nationalety>")
def Addsuccess(name,age,address,nationalety):
   return f"welcome {name} {age} {address} {nationalety}"

@app.route("/view",methods = ["POST","GET"])
def view():
   if request.method == "POST":
       name = request.form["name"]
       age = request.form["age"]
       address = request.form["address"]
       nationalety = request.form["nationalety"]
       return redirect(url_for("Addsuccess",name = name, age = age, address = address, nationalety = nationalety))
   
#=========  GET DATA =========
   name = request.args.get("name")
   age = request.args.get("age")
   address = request.args.get("address")
   nationalety = request.args.get("nationalety")
   return redirect(url_for("Addsuccess",name = name, age = age, address = address, nationalety = nationalety))

# Exercise 2
"""
DATABASE = "Stocks1.db"
app = Flask(__name__)

@app.route("/")
def index():
   with sql.connect(DATABASE) as con:
       cur = con.cursor()
   res = cur.execute("select * from stokes")
   return render_template("index.html", stockes = res)
"""
if __name__ == "__main__":
    app.run()
      

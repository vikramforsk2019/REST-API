#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:51:11 2020

@author: jagveer
"""

from flask import *  
app = Flask(__name__)  

@app.route('/')
def msg():
    return render_template('login.html')
  
@app.route('/login',methods = ['POST'])  
def login():  
      uname=request.form['uname']  
      passwrd=request.form['pass']  
      if uname=="ayush" and passwrd=="google":  
          return "Welcome %s" %uname  
      else:
          return render_template('message.html',name=uname,p=passwrd)

@app.route('/table/<int:num>')  
def table(num):  
      return render_template('table.html',n=num)  

   
if __name__ == '__main__':  
   app.run(debug = False)
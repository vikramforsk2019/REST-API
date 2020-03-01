#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:48:54 2020

@author: jagveer
"""
from flask import Flask, redirect, url_for, request 
app = Flask(__name__) 

@app.route('/home')  
def home():  
    return "hello, welcome to our website";  
  
if __name__ =="__main__":  
    app.run(debug = False)  
    

@app.route('/view/<name>') 
def hello_name(name_age): 
   return 'Hello %s!' % name_age

@app.route('/home2/<int:age>')  
def home2(age):  
    return "Age = %d"%age; 

def about():  
    return "This is about page";  
  
app.add_url_rule("/about2","about",about)  


@app.route('/success/<name>') 
def success(name): 
 return 'welcome %s' % name 


@app.route('/login',methods = ['POST', 'GET']) 
def login(): 
    if request.method == 'POST': 
    	user = request.form['nm'] 
    	return redirect(url_for('success',name = user)) 
    else: 
    	user = request.args.get('nm') 
    	return redirect(url_for('success',name = user)) 

if __name__ == '__main__': 
 app.run(debug = False) 

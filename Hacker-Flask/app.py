from flask import Flask, render_template, request, url_for
import json
import requests
from PIL import Image
import matplotlib.pyplot as plt


app = Flask(__name__)
host = "127.0.0.1"
port = 5000
debug = True
@app.route("/")
def home_page():
   response = requests.get("http://starlord.hackerearth.com/recipe")
   jsondata = response.json()
   with open("sample.json", "w") as outfile: 
   	json.dump(jsondata, outfile) 
   return render_template("index.html",len=len(jsondata),jsondata=jsondata)

@app.route("/service",methods=['GET', 'POST'])
def service():
	idd = request.args.get('id')
#as JSON only allows enclosing strings with double quotes you can manipulate the string like this:
#This will replace all occurrences of single quote with double quote in the JSON string str.
#Convert string dictionary to dictionary	
	idd=idd.replace("\'", "\"")
	res = json.loads(idd) 
	return render_template("services.html",s=res)




@app.route("/Contact",methods=['GET', 'POST'])
def contact():
   return render_template("contact.html")

@app.route("/About",methods=['GET', 'POST'])
def about():
   return render_template("about.html")

if __name__ == "__main__":
    app.run(debug = debug)

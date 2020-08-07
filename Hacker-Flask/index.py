from flask import Flask, render_template, request, url_for
import json
import requests
from PIL import Image
import matplotlib.pyplot as plt


app = Flask(__name__)
host = "127.0.0.1"
port = 5000
debug = True
@app.route("/home")
def home_page():
   response = requests.get("http://starlord.hackerearth.com/recipe")
   jsondata = response.json()
   return render_template("index.html",len=len(jsondata),jsondata=jsondata)

@app.route("/service_page",methods=['GET', 'POST'])
def service_page():
   return render_template("services.html")
if __name__ == "__main__":
    app.run(debug = debug)

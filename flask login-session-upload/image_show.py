
from flask import Flask, render_template, request
from scipy.misc import imread, imresize, imsave
import numpy as np
import re
import base64
import pickle
#import tensorflow as tf

# Initialize flask app
app = Flask(__name__)

def convertImage(imgData1):
	 imgstr = re.search(r'base64,(.*)', str(imgData1)).group(1)
	 with open('output.png', 'wb') as output:
		   output.write(base64.b64decode(imgstr))

@app.route('/')
def index():
 return render_template("upload_file.html")

@app.route('/predict', methods=['POST'])
def predict():
     imgData = request.get_data()
     print(imgData)
     
	 # make it the right siz
 
if __name__ == "__main__":
# run the app locally on the given port
	app.run(host='127.0.0.1', port=5000)
   
    
    
"""
Created on Tue Mar 10 17:34:01 2020

@author: jagveer
"""

from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("/upload_file.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        uname = request.form['uname']  
        f = request.files['file']  
        f.save(f.filename)  
        return render_template("success.html", name = f.filename,uname=uname)  
  
if __name__ == '__main__':  
    app.run(debug = False)  
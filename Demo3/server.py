# pip install flask
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

host = "127.0.0.1"
port = 5000
debug = True


@app.route("/home")
def home_page():
    return "<h1>Welcome to Forsk Technologies</h1>"

@app.route("/view")
def page_view():
    return render_template("user_form.html")


@app.route("/data1/<name>/<age>/<place>")
def input_type1(name, age,place):
    user_data = {"Name":name, "Age":age, "Place":place}
    return render_template("index.html", user=user_data)

@app.route("/data2")
def input_type2():
    name = request.args.get("Name")
    age = request.args.get("Age")
    place = request.args.get("Place")

    user_data = {"Name":name, "Age":age, "Place":place}
    return render_template("index.html", user=user_data)


@app.route("/data3", methods=["POST"])
def input_type3():
    name = request.json.get("Name")
    age = request.json.get("Age")
    place = request.json.get("Place")

    user_data = {"Name":name, "Age":age, "Place":place}
    return render_template("index.html", user=user_data)


@app.route("/data4", methods=["POST"])
def input_type4():
    name = request.form["Name"]
    age = request.form["Age"]
    place = request.form["Place"]

    user_data = {"Name":name, "Age":age, "Place":place}
    return render_template("index.html", user=user_data)

@app.route("/inp_form")
def show_form():
    return render_template("user_form.html")

if __name__ == "__main__":
    app.run(debug = debug)

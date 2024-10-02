import flask
from flask import Flask, render_template, redirect, request, jsonify

# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


# Route to render index.html template using data from Mongo

@app.route("/")
def index():
    return render_template("./templates/index.html")

@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/about_us")
def about_us():
    return render_template("templates/about_us.html")

@app.route("/tableau")
def tableau():
    return render_template("tableau1.html")


@app.after_request
def add_header(r):
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

# Main
if __name__ == "__main__":
    app.run(debug=True)


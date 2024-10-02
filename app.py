import flask
from flask import Flask, render_template, redirect, request, jsonify
import modelHelper
from modelHelper import ModelHelper

# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

modelHelper = ModelHelper()

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/tableau")
def tableau():
    return render_template("tableau1.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    content = request.json["data"]
    print(content)

    # Extract Title for the recommendation
    Title = content["Title"]

    recommended_movies = modelHelper.make_recommendation(Title)

    # Convert DataFrame to a JSON-compatible format
    recommended_movies_json = recommended_movies.to_dict(orient='records')

    return jsonify({"ok": True, "recommendations": recommended_movies_json})

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


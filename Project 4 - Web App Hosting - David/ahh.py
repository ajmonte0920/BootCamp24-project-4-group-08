from flask import Flask, render_template

# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Route to render home_page.html template
@app.route("/")
def index():
    return render_template("home_page.html")

@app.route("/home")
def home():
    return render_template("home_page.html")

@app.route("/about_us")
def index():
    return render_template("about_us.html")

@app.route("/tableau_ajm")
def index():
    return render_template("tableau(ajm dashboard).html")

@app.route("/tableau_jl")
def index():
    return render_template("tableau(jl dashboard).html")

@app.route("/gradio")
def index():
    return render_template("gradio.html")

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


# Main
if __name__ == "__main__":
    app.run(debug=True)








from flask import Flask, render_template
import gradio as gr
import threading

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
def about_us():
    return render_template("about_us.html")

@app.route("/tableau_ajm")
def tableau_ajm():
    return render_template("tableau(ajm dashboard).html")

@app.route("/tableau_jl")
def tableau_jl():
    return render_template("tableau(jl dashboard).html")

# route for Gradio
@app.route("/gradio")
def gradio_page():
    return render_template("gradio.html")

# Launch Gradio app in a separate thread
def launch_gradio():
    def greet(name):
        return f"Hello, {name}!"

    iface = gr.Interface(fn=greet, inputs="text", outputs="text")
    iface.launch(share=False, server_name="0.0.0.0", server_port=7860, inline=False)

threading.Thread(target=launch_gradio).start()

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










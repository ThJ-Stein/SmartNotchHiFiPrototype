from flask import Flask
app = Flask(__name__)

state = "none"

@app.route("/")
def hello():
	return "Hello world!"

@app.route("/smartnotch")
def serve_smartnotch():
	#code for serving the html page for smartnotch

@app.route("/majorlaser")
def serve_majorlaser():
	#code for serving the html page for major laser

@app.route("/controller")
def serve_controller():
	#code for serving the html page for controller

@app.route("/api", methods=["POST"])
def post_message():
	#code for handling a post request
	#state = request.getString() <-- pseudocode

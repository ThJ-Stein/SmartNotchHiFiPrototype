from flask import Flask
from PublicIP import IP
app = Flask(__name__)

state = "none"

@app.route("/")
def hello():
	return "Hello world!"

@app.route("/smartnotch")
def serve_smartnotch():
	#code for serving the html page for smartnotch
	return "not yet implemented"

@app.route("/majorlaser")
def serve_majorlaser():
	#code for serving the html page for major laser
	return "not yet implemented"

@app.route("/controller")
def serve_controller():
	#code for serving the html page for controller
	return "not yet implemented"

@app.route("/api", methods=["POST"])
def post_message():
	#code for handling a post request
	#state = request.getString() <-- pseudocode
	return "not yet implemented"

if __name__ == "__main__":
	print IP()
	app.run(IP(),5000)

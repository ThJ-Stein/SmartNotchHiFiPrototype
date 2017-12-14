from flask import Flask, request
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

@app.route("/api", methods=["GET", "POST"])
def request_api():
	global state
	if request.method == "POST":
		state = request.get_data()
		return "HTTP 200: successful", 200
	elif request.method == "GET":
		return state, 200

def post_api(request):
	print(request.data)
	return request.data

def get_api(request):
	return state

if __name__ == "__main__":
	print IP()
	app.run(IP(),5000)

from flask import Flask, render_template, request
from flask_sse import sse
from PublicIP import IP

app = Flask(__name__)
app.register_blueprint(sse, url_prefix='/sse')

@app.route("/")
def hello():
	return render_template('index.html')

@app.route("/smartnotch")
def serve_smartnotch():
	#code for serving the html page for smartnotch
	return render_template('notch.html')

@app.route("/majorlaser")
def serve_majorlaser():
	#code for serving the html page for major laser
	return render_template('laser.html')

@app.route("/controller")
def serve_controller():
	#code for serving the html page for controller
	return render_template('controller.html')

@app.route("/api", methods=["GET", "POST"])
def request_api():
	global state
	if request.method == "POST":
		sse.publish({"message": request.get_data()}, type="state")
		return "HTTP 200: successful", 200

if __name__ == "__main__":
	print IP()

app.run(IP(), 80)
exit()

from flask import Flask, render_template, request
from flask_sse import sse
from PublicIP import IP
import json

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

@app.route("/api", methods=["POST"])
def request_api():
	if request.method == "POST":
		content = request.get_json()
		print content
		scenario = content["mode"] + content["option"]
		with open("data.json") as f:
			d = json.loads(f.read());
		if not scenario in d.keys():
			d[scenario] = []
		d[scenario].append([content["yesorno"], content["rating"]])

		with open("data.json", 'w') as f:		
			f.write(json.dumps(d))

		print d
		return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

if __name__ == "__main__":
	print IP()

app.run(IP(), 5000)
exit()

#!/usr/bin/env python3

from flask import (
	Flask,
	request,
	jsonify,
	render_template
)


app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/version', methods=['GET'])
def app_version():
	commitid = open('/app/commit_id','r').readlines()[0].strip()
	data = {
			"Rena-Application": [
				{
					"version":"1.0.0",
					"lastcommithash":commitid,
					"description":"Test application"
				}
			]
		}
	return data

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')
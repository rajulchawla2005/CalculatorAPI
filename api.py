import calculator
from flask import Flask, render_template, url_for, redirect, request, jsonify, after_this_request
import json

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")
	
@app.route("/buttons")
def add_button():
	return render_template("buttons/add_button.html")
def sub_button():
	return render_template("buttons/sub_button.html")
def mul_button():
	return render_template("buttons/mul_button.html")
def div_button():
	return render_template("buttons/div_button.html")
	
@app.route('/api_call_get', methods=['GET', 'POST'])
def get_test():
	if request.method == 'GET':
		jsonResp = {"bro what are you tryna get??":1}
		print(jsonResp)
		return jsonify(jsonResp)
	else:
		print("bad request, get test")
		return "Too sigma", 400

@app.route('/api_call_add_post', methods=['GET', 'POST'])
def add_post_call():
	if request.method == 'POST':
		inputs = request.data.decode("UTF-8")
		json_dict = json.loads(inputs)
		num1, num2 = json_dict['num1'], json_dict['num2']
		answer = calculator.add(num1, num2)
		jsonResp = {"output":answer}
		print(jsonResp)
		return jsonify(jsonResp)
	else:
		print("bad request, add post call")
		return "Too sigma", 400	

	
if __name__ == "__main__":
	with app.test_request_context():
		home_url = url_for('home')
		
		print("home_urL:", home_url)
		app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)

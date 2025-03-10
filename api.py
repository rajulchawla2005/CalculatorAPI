import calculator
from flask import Flask, render_template, url_for, redirect

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

	
if __name__ == "__main__":
	with app.test_request_context():
		home_url = url_for('home')
		
		print("home_urL:", home_url)
		app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)

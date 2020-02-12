from flask import Flask, redirect, render_template, url_for

from pyA20.gpio import gpio
from pyA20.gpio import port
led = port.PA14
gpio.init()
gpio.setcfg(led,gpio.OUTPUT)
gpio.output(led,0)

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/automate')
def automate():
	return render_template("automate.html")

@app.route('/<deviceName>/<action>')
def control(deviceName,action):
	if deviceName == 'led':
		device = led
	if action == "on":
		gpio.output(device,1)
	if action == "off":
		gpio.output(device,0)
	return redirect(url_for('automate'))

@app.route('/biz_barada')
def about():
	class User:
		def  __init__(self, username, salary):
			self.username = username
			self.salary = salary
			
	user1 = User("Plan Planyyew", 4200)
	user2 = User("Wepa Mekanow", 3000)

	users = {
		'first': user1,
		'second': user2,
	}

	return render_template("about.html", **users)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)

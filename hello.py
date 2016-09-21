from flask import Flask

app= Flask(__name__)

@app.route("/")
def thing0():
	return __name__+" hello"

@app.route("/1")
def thing1():
	return "how are you"

@app.route("/2")
def thing2():
	return "doing today?"

if __name__=="__main__":
	app.run()


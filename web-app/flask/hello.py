from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

# No prompt de comando digite:
# export FLASK_APP=hello.py
# $ flask run
# * Running on http://127.0.0.1:5000/
# copy e cole a url acima.

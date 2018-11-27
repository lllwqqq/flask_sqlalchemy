from flask import Flask,session
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def hello_world():
    session['username'] = 'AromaSession'
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

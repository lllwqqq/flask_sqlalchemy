from flask import Flask,current_app

app = Flask(__name__)


aa = '123'

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.before_first_request
def before_first_request():
    print('before_first_request, %s' %aa)


@app.before_request
def before_request():
    print('在试图函数执行前执行的钩子函数')


if __name__ == '__main__':
    app.run()

from flask import Flask,current_app,render_template

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!'


@app.before_first_request
def before_first_request():
    print('在第一次请求视图函数之前执行的钩子函数')


@app.before_request
def before_request():
    print('在每次请求视图函数执行前执行的钩子函数')


@app.errorhandler(404)
def errorhandler(error):
    return render_template('404.html'),404
    print('您请求的页面可能丢在火星了~')

if __name__ == '__main__':
    app.run()

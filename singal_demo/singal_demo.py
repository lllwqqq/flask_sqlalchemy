from flask import Flask,request,g
from singals import loginsingal
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login/')
# def login():
#     username = request.args.get('username')
#     if username:
#         # 第一种把变量传给信号的方法，这里send给loginsingal，后面就需要接收username
#         #loginsingal.send(username=username)
#         return '登陆成功！'
#     else:
#         return "请输入用户名"
def login():
    username = request.args.get('username')
    if username:
        # 第二种方法是用g对象
        g.username = username
        loginsingal.send()
        return '登陆成功！'
    else:
        return "请输入用户名"



if __name__ == '__main__':
    app.run()

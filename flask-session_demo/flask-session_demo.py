from flask import Flask,session
import os
from datetime import timedelta
app = Flask(__name__)

# 要用session,必须设置SECRET_KEY
app.config['SECRET_KEY'] = os.urandom(24)

# 配置session过期时间,在创建session的函数中需要用session.permanent = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)

# 创建session
@app.route('/')
def hello_world():
    session['username'] = 'AromaSession'
    session.permanent = True
    return 'Hello World!'

# 获取session
@app.route('/getsession/')
def getSession():
    username = session.get('username')
    return username or '没有获取到session'

# 删除session
@app.route('/delsession/')
def delSession():

    session.pop('username')
    # 删除所有session
    #session.clear()
    return '删除Session成功'




if __name__ == '__main__':
    app.run()

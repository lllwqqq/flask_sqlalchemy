from flask import Flask,Request,Response

app = Flask(__name__)


@app.route('/')
# 创建Cookie
# def add_cookie():
#     resp = Response('创建Cookie')
#     resp.set_cookie('username',value='Aroma',max_age=60)
#     return resp
# 设置Cookie有效期
def expireCookie():
    resp = Response('Cookie有效期测试')
    # max_age 在IE8以下不生效，expires被视为废弃参数，且时间为格林尼治时间，但几乎所有浏览器都还支持，当两个参数都设置后，max_age参数生效，两个参数都未设置后，以关闭浏览器为过期时间
    # PS:格林尼治时间减去8小时，即为北京时间，如：你想设置过期时间为2018-11-11 00：00：00过期，那expires就设置为2018-11-10 16：00：00
    resp.set_cookie('username',value='Aroma',max_age=60)
    return resp


@app.route('/delcookie/')
def del_cookie():
    resp = Response('删除Cookie')
    resp.delete_cookie('username')
    return resp



if __name__ == '__main__':
    app.run()

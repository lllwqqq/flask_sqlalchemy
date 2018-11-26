from flask import Flask,Request,Response

app = Flask(__name__)


@app.route('/')
def add_cookie():
    resp = Response('创建Cookie')
    resp.set_cookie('username',value='Aroma',expires=15)
    return resp

@app.route('/delcookie/')
def del_cookie():
    resp = Response('删除Cookie')
    resp.delete_cookie('username')
    return resp


if __name__ == '__main__':
    app.run()

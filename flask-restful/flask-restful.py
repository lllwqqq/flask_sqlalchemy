from flask import Flask
from flask_restful import Api,Resource,reqparse

app = Flask(__name__)
api = Api(app)


class LoginView(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('username',type=str,help='用户名验证错误！',required = True)
        parse.add_argument('password',type=str,help='密码验证错误！')
        parse.add_argument('gender',type=int,help='密码验证错误！',choices=['male','gmale','secret'])
        args = parse.parse_args()
        print('username: %s' %args['username'])
        print('password: %s' %args['password'])
        return {'username': args['username']}

api.add_resource(LoginView,'/login/',endpoint='login')

@app.route('/')
def index():
    return '首页!'


if __name__ == '__main__':
    app.run(debug=True)

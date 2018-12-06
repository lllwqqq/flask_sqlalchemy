from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)


class LoginView(Resource):
    def post(self):
        return {'username':'Aroma'}

api.add_resource(LoginView,'/login/',endpoint='login')

@app.route('/')
def index():
    return '首页!'


if __name__ == '__main__':
    app.run(debug=True)

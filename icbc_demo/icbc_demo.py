from flask import Flask,views,render_template,request
from forms import RegistForm
from exts import db
import config
from models import User

app = Flask(__name__)
db.init_app(app)
app.config.from_object(config)

@app.route('/')
def index():
    return render_template('index.html')



class RegistViews(views.MethodView):
    def get(self):
        return render_template('regist.html')
    def post(self):
        form = RegistForm(request.form)
        if form.validate():
            deposit = form.deposit.data
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = User(deposit=deposit,email=email,username=username,password=password)
            db.session.add(user)
            db.session.commit()
            return '注册成功!'
        else:
            print(form.errors)
            return '注册失败!'
app.add_url_rule('/regist/',view_func=RegistViews.as_view('regist'))


if __name__ == '__main__':
    app.run()

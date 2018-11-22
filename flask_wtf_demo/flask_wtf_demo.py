from flask import Flask,request,render_template
from forms import RegistForm,LoginForm,SettingsForm

app = Flask(__name__)




@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        form = RegistForm(request.form)
        if form.validate():
            return 'success!!!'
        else:
            print(form.errors)
            return 'Failed'





@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        forms = LoginForm(request.form)
        if forms.validate():
            return 'success'
        else:
            return 'failed'


@app.route('/settings/',methods=['GET','POST'])
def settings():
    if request.method == 'GET':
        form = SettingsForm()
        return render_template('settings.html',form=form)
    else:
        form = SettingsForm(request.form)
        return 'fail'


if __name__ == '__main__':
    app.run(debug=True)

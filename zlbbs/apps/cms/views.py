# coding=utf-8
from flask import Blueprint,views,render_template,request,session,redirect,url_for
from .forms import LoginForm
from .models import CMSUser

bp = Blueprint("cms",__name__,url_prefix="/cms")

@bp.route('/')
def index():
    return "cms index"

class LiginView(views.MethodView):
    def get(self,message=None):
        return render_template('cms/cms_login.html',message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session['user_id'] = user.id
                if remember:
                    # 默认过期时间为31天
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                message = form.errors.popitem()[1][0]
                return self.get(message=message)
        else:
            print(form.errors)
            message = form.errors.popitem()[1][0]
            return self.get(message=message)

bp.add_url_rule('/login/',view_func=LiginView.as_view('login'))
# coding=utf-8
from flask import Blueprint,views,render_template,request,session,redirect,url_for,g,jsonify
from .forms import LoginForm,ResetPwdForm
from .models import CMSUser
from .decorators import login_required
import config
from exts import db


bp = Blueprint("cms",__name__,url_prefix="/cms")

@bp.route('/')
@login_required
def index():
    return render_template('cms/cms_index.html')


@bp.route('/logout/')
@login_required
def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for('cms.login'))

@bp.route('/setting/')
@login_required
def setting():
    return render_template('cms/cms_setting.html')

@bp.route('/profile/')
@login_required
def profile():
    return render_template('cms/cms_profile.html')


@bp.route('/myhome/')
@login_required
def myhome():
    return render_template('cms/cms_my_hone.html')

@bp.route('/card/')
@login_required
def card():
    return render_template('cms/cms_card.html')

@bp.route('/users/')
@login_required
def cms_users():
    return render_template('cms/cms_users.html')

@bp.route('/ausers/')
@login_required
def cms_ausers():
    return render_template('cms/cms_ausers.html')

@bp.route('/groups/')
@login_required
def cms_groups():
    return render_template('cms/cms_groups.html')

@bp.route('/agroups/')
@login_required
def cms_agroups():
    return render_template('cms/cms_agroups.html')

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
                session[config.CMS_USER_ID] = user.id
                if remember:
                    # 默认过期时间为31天,config配置文件中可配置，参数为PERMANENT_SESSION_LIFETIME = ''
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                message = form.errors.popitem()[1][0]
                return self.get(message=message)
        else:
            print(form.errors)
            message = form.errors.popitem()[1][0]
            return self.get(message=message)


class ResetPwdView(views.MethodView):
    decorators = [login_required]
    def get(self):
        return render_template('cms/cms_resetpwd.html')

    def post(self):
        resetpwd_form = ResetPwdForm(request.form)
        if resetpwd_form.validate():
            oldpwd = resetpwd_form.oldpwd.data
            newpwd = resetpwd_form.newpwd.data
            user = g.cms_user
            if user.check_password(oldpwd):
                user.password = newpwd
                db.session.commit()
                #因为接受的是ajax,所以这里使用jsonify返回数据
                #返回code字段表示状态码，message信息提示
                return jsonify({"code": 200, "message":"修改成功"})
            else:
                return jsonify({"code": 400, "message": "原密码错误"})
        else:
            message = resetpwd_form.get_error()
            return jsonify({"code": 400, "message":message})


bp.add_url_rule('/resetpwd/', view_func=ResetPwdView.as_view('resetpwd'))


bp.add_url_rule('/login/',view_func=LiginView.as_view('login'))
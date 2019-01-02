# coding=utf-8
from flask import Blueprint,views,render_template,request,session,redirect,url_for,g,jsonify
from .forms import LoginForm, ResetPwdForm, RestEmailForm
from .models import CMSUser
from .decorators import login_required
import config,string,random
from exts import db,mail
from utils import xjson,xcache
from flask_mail import Message

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
                return xjson.json_success('修改成功')
            else:
                return xjson.json_paramserror('原密码错误')
        else:
            message = resetpwd_form.errors
            return xjson.json_paramserror(message.popitem()[1][0])

class ResetEmailView(views.MethodView):
    decorators = [login_required]
    def get(self):
        return render_template('cms/cms_resetemail.html')

    def post(self):
        resetemail_form = RestEmailForm(request.form)
        if resetemail_form.validate():
            email = resetemail_form.email.data
            g.cms_user.email = email
            db.session.commit()
            return xjson.json_success('邮箱修改成功')
        else:
            message = resetemail_form.errors()
            return xjson.json_paramserror(message)

@bp.route('/email_captcha/')
@login_required
def email_captcha():
    email = request.args.get('email')
    if not email:
        return xjson.json_paramserror('请传递邮件参数')

    #生成6位数的随机验证码
    source = list(string.ascii_letters)
    source.extend(map(lambda x:str(x),range(0,10)))
    captcha = ''.join(random.sample(source,6))

    #发送验证码邮件
    msg = Message('BBS论坛更换邮箱验证码',
                  recipients=[email],
                  body='您的验证码是：{}，5分钟内有效'.format(captcha)
                  )
    try:
        mail.send(msg)
    except Exception as err:
        print(err)
        return xjson.json_servererror(message='邮件发送失败')

    # 验证码存入memcache
    print(email+'*'*10+captcha)
    xcache.set(email, captcha)
    return xjson.json_success(message='邮件发送成功')


#测试邮件发送方法
@bp.route('/test_email/')
def test_email():
    msg = Message('Flask项目测试邮件', #邮件主题
                  sender='972092009@qq.com', #发送邮箱
                  recipients=['lllwqqq@163.com'], #接收邮箱，这是个列表，可以有多个接收者
                  body='Hello，这是一封测试邮件，这是正文'
                   )
    mail.send(msg)
    return '发送成功'


bp.add_url_rule('/login/',view_func=LiginView.as_view('login'))
bp.add_url_rule('/resetpwd/',view_func=ResetPwdView.as_view('resetpwd'))
bp.add_url_rule('/resetemail/',view_func=ResetEmailView.as_view('resetemail'))

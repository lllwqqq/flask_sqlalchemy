# coding=utf-8
from wtforms import Form,StringField,IntegerField
from wtforms.validators import Email,InputRequired,Length,EqualTo,ValidationError
from .models import CMSUser
from utils import xcache

class LoginForm(Form):
    email = StringField(validators=[Email(message='请输入正确的邮箱!'),InputRequired(message='请输入邮箱!')])
    password = StringField(validators=[Length(6,20,message='请输入正确的密码!')])
    remember = IntegerField()


class ResetPwdForm(Form):
    oldpwd = StringField(validators=[Length(6,30, message='密码长度6-30')])
    newpwd = StringField(validators=[Length(6,30, message='密码长度6-30')])
    newpwd2 = StringField(validators=[EqualTo('newpwd', message='新密码输入不一致')])


class RestEmailForm(Form):
    email = StringField(validators=[Email(message='邮箱格式错误'),InputRequired(message='请输入邮箱') ])
    captcha = StringField(validators=[Length(min=6, max=6, message='验证码长度错误')])

    def validate_email(self, field):
        user = CMSUser.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError('该邮箱已存在')

    def validate_captcha(self, field):
        email = self.email.data
        captcha = field.data
        captcha_cache = xcache.get(email)
        #判断memcached中是否有对应的邮箱及验证码，小写进行比较，这样用户可以不区分大小写
        if  not captcha_cache or captcha.lower() != captcha_cache.lower():
            raise ValidationError('邮箱验证码错误')
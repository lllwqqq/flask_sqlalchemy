# coding=utf-8
from wtforms import Form,StringField,IntegerField
from wtforms.validators import Email,InputRequired,Length,EqualTo

class LoginForm(Form):
    email = StringField(validators=[Email(message='请输入正确的邮箱!'),InputRequired(message='请输入邮箱!')])
    password = StringField(validators=[Length(6,20,message='请输入正确的密码!')])
    remember = IntegerField()


class ResetPwdForm(Form):
    oldpwd = StringField(validators=[Length(6,30, message='密码长度6-30')])
    newpwd = StringField(validators=[Length(6,30, message='密码长度6-30')])
    newpwd2 = StringField(validators=[EqualTo('newpwd', message='新密码输入不一致')])
# coding=utf-8

from wtforms import Form,StringField,IntegerField,BooleanField,SelectField
from wtforms.validators import Length,EqualTo,Email,InputRequired,NumberRange


class RegistForm(Form):
    username = StringField(validators=[Length(min=3,max=6,message='用户名为3~6个字符!')])
    password = StringField(validators=[Length(min=3,max=10,message='密码长度为3~10个字符!')])
    password_comfirm = StringField(validators=[Length(min=3,max=10,message='两次密码不匹配!'),EqualTo('password')])


class LoginForm(Form):
    email = StringField(validators=[Email()])


class SettingsForm(Form):
    username = StringField('用户名：',validators=[Length(min=3,max=8),InputRequired])
    age = IntegerField('年龄：',validators=[NumberRange(18,100)])
    rememberMe = BooleanField('记住我:')
    tags = SelectField('标签:',choices=[('1','Python'),('2','Java'),('3','Php')])
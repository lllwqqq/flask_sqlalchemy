# coding=utf-8
from wtforms import Form,StringField,FloatField
from wtforms.validators import Email,EqualTo,Length,InputRequired,number_range

class RegistForm(Form):
    email = StringField(validators=[Email()])
    username = StringField(validators=[Length(3,10)])
    password = StringField(validators=[Length(6,18)])
    password_repeat = StringField(validators=[EqualTo('password')])
    deposit = FloatField(validators=[InputRequired()])


class LoginForm(Form):
    email = StringField(validators=[Email()])
    password = StringField(validators=[Length(6,18)])


class TransferForm(Form):
    email = StringField(validators=[Email()])
    money = FloatField(validators=[number_range(1,20000)])
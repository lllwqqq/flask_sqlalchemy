# coding=utf-8
from wtforms import Form,StringField,FloatField
from wtforms.validators import Email,EqualTo,Length,InputRequired

class RegistForm(Form):
    email = StringField(validators=[Email()])
    username = StringField(validators=[Length(3,10)])
    password = StringField(validators=[Length(6,18)])
    password_repeat = StringField(validators=[EqualTo('password')])
    deposit = FloatField(validators=[InputRequired()])
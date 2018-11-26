# coding=utf-8
from flask_wtf import Form
from wtforms import FileField,StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired,FileAllowed


class UploadForm(Form):
    avatar = FileField('上传文件:',validators=[FileRequired(),FileAllowed(['jpg','png','gif'])])
    desc = StringField(validators=[InputRequired()])
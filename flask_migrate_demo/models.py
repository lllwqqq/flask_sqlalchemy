# coding=utf-8
from exts import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(50),nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(20),nullable=False)
    context = db.Column(db.Text)

# coding=utf-8
# coding=utf-8
import os
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'restful_demo2'
USERNAME = 'root'
PASSWORD = 'coursedev'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.urandom(24)
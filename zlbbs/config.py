# coding=utf-8
import os
SECRET_KEY = os.urandom(24)

DEBUG = True

HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'zlbbs'
USERNAME = 'root'
PASSWORD = 'coursedev'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False

# PERMANENT_SESSION_LIFETIME = '1800'
CMS_USER_ID = 'SFASDFSAFASDFSAF'


#邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = '465'
MAIL_USE_SSL = True #使用SSL，端口号为465或587
MAIL_USERNAME = '972092009@qq.com'
MAIL_PASSWORD = 'cobctytfgeawbcgh'   #注意，这里的密码不是邮箱密码，而是授权码
MAIL_DEFAULT_SENDER = '972092009@qq.com'  #默认发送者
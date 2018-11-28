# coding=utf-8
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from icbc_demo import app
from exts import db
# 如果不导入，则会在migrate的时候，找不到模型，就不会生成相应的表
from models import User


manage = Manager(app)

Migrate(app,db)

manage.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manage.run()

# coding=utf-8
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from zlbbs import create_app
from exts import db
from apps.cms import models as cms_models
CMSUser = cms_models.CMSUser
app = create_app()

manage = Manager(app)

Migrate(app,db)
manage.add_command('db',MigrateCommand)

@manage.option('-u','--username',dest='username')
@manage.option('-p','--password',dest='password')
@manage.option('-e','--email',dest='email')
def create_cms_user(username,password,email):
    user = CMSUser(username=username,password=password,email=email)
    db.session.add(user)
    db.session.commit()
    print("CMS用户添加成功!!!")



if __name__ == '__main__':
    manage.run()
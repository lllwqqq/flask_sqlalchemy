# coding=utf-8
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from zlbbs import create_app
from exts import db
from apps.cms import models as cms_models
CMSUser = cms_models.CMSUser
CMSRole = cms_models.CMSRole
CMSPermission = cms_models.CMSPermission
app = create_app()

manager = Manager(app)

Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')
@manager.option('-e','--email',dest='email')
def create_cms_user(username,password,email):
    user = CMSUser(username=username,password=password,email=email)
    db.session.add(user)
    db.session.commit()
    print("CMS用户添加成功!!!")


@manager.command
def create_cms_role():
    # 1. 访问者
    visitor = CMSRole(name='访问者',desc='只能访问，不能修改数据')
    visitor.permissions = CMSPermission.VISITOR

    # 2. 运营
    operator = CMSRole(name='运营',desc='管理帖子、评论、前台用户')
    operator.permissions = CMSPermission.VISITOR|CMSPermission.CMSUSER|CMSPermission.COMMENTER|CMSPermission.POSTER|CMSPermission.FRONTUSER

    # 3. 管理员
    admin = CMSRole(name='管理员',desc='拥有绝大部分权限')
    admin.permissions = CMSPermission.VISITOR|CMSPermission.CMSUSER|CMSPermission.COMMENTER|CMSPermission.POSTER|CMSPermission.FRONTUSER|CMSPermission.BOARDER

    # 4. 开发人员
    developer = CMSRole(name='超级管理员',desc='开发小哥专用，拥有至高无上的权限')
    developer.permissions = CMSPermission.ALL_PERMISSION

    db.session.add_all([visitor,operator,admin,developer])
    db.session.commit()

@manager.option('-e','--email',dest='email')
@manager.option('-n','--name',dest='name')
def add_user_to_role(email,name):
    user = CMSUser.query.filter_by(email=email).first()
    if user:
        role = CMSRole.query.filter_by(name=name).first()
        if role:
            role.users.append(user)
            db.session.commit()
            print('用户添加到角色成功')
        else:
            print('没有这个角色')
    else:
        print('%s 邮箱没有这个用户' %email)


@manager.command
def test_permission():
    user = CMSUser.query.first()
    if user.has_permission(CMSPermission.VISITOR):
        print('这个用户有访问者权限！')
    else:
        print('这个用户没有访问者权限!')

if __name__ == '__main__':
    manager.run()
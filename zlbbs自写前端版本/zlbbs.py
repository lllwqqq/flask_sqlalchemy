from flask import Flask
from apps.common.views import bp as common_bp
from apps.cms.views import bp as cms_bp
from apps.front.views import bp as front_bp
import config
from exts import db
from flask_wtf import CSRFProtect


def create_app():

    app = Flask(__name__)
    app.config.from_object(config)
    # config.py 配置文件
    # exts.py 装载第三库的实例对象的文件
    # models 模型文件
    # manage.py 项目运行文件
    # app包，存储蓝图(前端、后端、公共)
    app.register_blueprint(common_bp)
    app.register_blueprint(cms_bp)
    app.register_blueprint(front_bp)
    db.init_app(app)
    CSRFProtect(app)
    return app



if __name__ == '__main__':
    app=create_app()
    app.run()

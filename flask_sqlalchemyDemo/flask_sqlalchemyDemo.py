from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import MigrateCommand,Migrate,Manager


app = Flask(__name__)

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask_sqlalchemy_demo'
USERNAME = 'root'
PASSWORD = 'coursedev'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4".format(username=USERNAME,password=PASSWORD,
                                                                                           host=HOSTNAME,port=PORT,db=DATABASE)

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


class UserModel(db.Model):
    # 如果不指定__tablename__，flask会以大写字母为标识来用_分隔创建默认表名
    # 如：UserModel ，则默认创建的表为user_model
    __tablename__ = 'user_model'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(10),nullable=False)

    def __repr__(self):
        return '<USERNAME: %s>' %self.username

class ArticleModel(db.Model):
    __tablename__ = 'article_model'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(50),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("user_model.id"))
    author = db.relationship("UserModel",backref='articles')

# 创建数据库
# db.drop_all()
# db.create_all()

# 添加数据
# user = UserModel(username='Aroma2')
# article = ArticleModel(title='title2')
# article.author = user
# db.session.add(article)
# db.session.commit()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

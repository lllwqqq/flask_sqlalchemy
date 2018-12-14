from flask import Flask
from exts import db
import config
from models import User,Ariticle,Tag
from flask_restful import Resource, Api, reqparse, marshal_with, fields


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
api = Api(app)
class ArticleView(Resource):


    resource_fields = {
        # attribute: 重命名属性,比如这里，我们的models里面是没有article_title字段的，所有用attribute属性来指定真正的字段名
        'article_title': fields.String(attribute='title'),
        'content': fields.String,
        'author': fields.Nested({
                'username':fields.String,
                'email':fields.String,
        }),
        'tags': fields.List(fields.Nested({
            'id': fields.Integer,
            'name':fields.String,
        })),
        # default: 指定默认值
        'reader_count': fields.Integer(default=0)
    }
    @marshal_with(resource_fields)
    def get(self,article_id):
        article = Ariticle.query.get(article_id)
        return article


api.add_resource(ArticleView,'/article/<article_id>/',endpoint='article')

@app.route('/')
def hello_world():
    user = User(username='Aroma',email='qq@qq.com')
    article = Ariticle(title='三国演义',content='西游记')
    article.author =  user
    tag1 = Tag(name='Python')
    tag2 = Tag(name='Java')
    article.tags.append(tag1)
    article.tags.append(tag2)
    db.session.add(article)
    db.session.commit()
    return '首页'


if __name__ == '__main__':
    app.run()

# coding=utf-8
from flask import Blueprint,render_template,make_response
from flask_restful import fields, marshal_with, Resource

from models import Ariticle
from flask_restful import Resource, Api, reqparse, marshal_with, fields

article_bp = Blueprint('article',__name__,url_prefix='/article')
api = Api(article_bp)


# 解决在蓝图中reder_template返回html代码的问题
@api.representation('text/html')
def output_html(data,code,headers):
    # 在representation装饰的函数中，必须返回一个Response对象
    resp = make_response(data)
    return resp


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



class ListView(Resource):
    def get(self):
        return render_template('article_list.html')

api.add_resource(ArticleView,'/<article_id>/',endpoint='article')
api.add_resource(ListView,'/list/',endpoint='article_list')
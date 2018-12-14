from flask import Flask
from exts import db
import config
from models import User,Ariticle,Tag
from articleviews import article_bp


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
app.register_blueprint(article_bp)




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

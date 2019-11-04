from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/pythonclass'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////text.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'xxxx'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100) )
    author = db.Column(db.String(20),nullable=True)
    content = db.Column(db.String(5000), nullable=True)

    def __init__(self, title, author,content ):
        self.title = title
        self.author = author
        self.content = content


    def __repr__(self):
        return '<User %r>' % self.author


db.create_all()

def commit(title,username,content):
    blog = User(title, username, content)
    db.session.add(blog)
    db.session.commit()
    return True

commit('永夜君王','烟雨江南','''永夜大陆大部分时间都是暮色昏昏，特别到了暗季，上层大陆的运行轨道遮挡住阳光，白昼只有短短的几个小时。今夜双子阿尔法星转入近地轨道，是个难得有月亮的晚上。''')
commit('静夜思','李白','''床前明月光，疑是地上霜。举头望明月，低头思故乡。''')
commit('圣墟','辰东','''在破败中崛起，在寂灭中复苏。 沧海成尘，雷电枯竭，那一缕幽雾又一次临近大地，世间的枷锁被打开了，一个全新的世界就此揭开神秘的一角……''')
if __name__ == '__main__':
    app.run()

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from config import *

db = SQLAlchemy()


# 数据库初始化函数,初始化时需要调用一次
def init(app):
    global db
    app.config
    db.init_app(app)


class User(db.Model):

    u_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(12),name='u_name')
    u_password = db.Column(db.String(12))
    u_nickname = db.Column(db.String(12))
    u_email = db.Column(db.String(100))  # 使用String类型替换EmailField


class History(db.Model):
    h_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    h_date = db.Column(db.Date)
    h_imagePath_before = db.Column(db.Text)
    h_imagePath_after = db.Column(db.Text)
    d_result = db.Column(db.String(20))
    d_advise = db.Column(db.Text)
    uid = db.Column(db.Integer, db.ForeignKey('user.u_id'))  # 定义外键关系
    user = relationship("User", back_populates="history")  # 声明关系属性

User.history = relationship("History", back_populates="user")  # 声明关系属性

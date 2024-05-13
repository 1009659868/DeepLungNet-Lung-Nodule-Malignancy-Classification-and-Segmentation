from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from sqlalchemy import create_engine
from config import *
app=Flask(__name__)




app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
engine=create_engine(DB_URL)

# 定义数据库模型
class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    # 在这里定义其他列...

# 测试是否连接成功
with app.app_context():
    with db.engine.connect() as conn:
        # 使用SQLAlchemy的select函数来执行查询
        stmt = select('*').select_from(Test)
        rs = conn.execute(stmt)
        for item in rs:
            print(item)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)








# usr/bin/python
# coding: UTF-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/db_shane'

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    create_at = db.Column(db.DateTime(timezone=True)) # 需要加上timezone，否则报错
    update_at = db.Column(db.DateTime(timezone=True))
    is_valid = db.Column(db.Integer, nullable=False,default=1)
    commts = db.relationship('Comment', backref='News',lazy='dynamic')

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    newsID = db.Column(db.Integer,db.ForeignKey('news.id')) # 设置外键
    content = db.Column(db.String(2000), nullable=False)
    create_at = db.Column(db.DateTime(timezone=True))
    is_valid = db.Column(db.Integer, nullable=False,default=1)


if __name__ == '__main__':
    app.run(debug=True)










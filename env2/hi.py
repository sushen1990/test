# usr/bin/env python
# coding:utf-8

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__) # 创建实例

@app.route("/")      # 当浏览器指向此地址
def index():         # 要做的事情
    """方法注释"""
    return render_template("admin.html")

@app.route("/<classfy>") # 当浏览器地址为"home/a",<classfy>的值就是a，这里相当于传递参数了
def toClassfy(classfy):
    return render_template("baidu/classfy.html", classfy=classfy) 

@app.route("/<classfy>/<news>") # 详情页面
def toNews(classfy,news):
	return render_template("baidu/news.html", classfy=classfy ,news=news)

app.secret_key = "sdgh_APOMBde"
if __name__ == '__main__':
    app.run(debug=True)
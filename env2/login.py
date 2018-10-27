from flask import Flask, render_template
from NewsForm import News, Comment
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app) # db是必须要引入的
app.config["SECRET_KEY"] = 'gfbfdg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/db_shane'


@app.route("/")
def login():
    """登陆首页"""
    return render_template("base.html") # 注意这里form就是定义好的类

@app.route("/admin/")
def login1():
    """登陆首页"""
    news_list = News.query.all()
    return render_template("admin.html", news_list=news_list) # 注意这里form就是定义好的类

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, url_for , flash , redirect , abort
from NewsForm import News, Comment
from forms import Form_news
from flask import Flask, render_template, url_for
from NewsForm import News, Comment
from forms import Form_news
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
db = SQLAlchemy(app) # db是必须要引入的
app.config["SECRET_KEY"] = 'gfbfdg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/db_shane'




@app.route("/")
def login1():
    """登陆首页"""
    news_list = News.query.all()
    return render_template("admin.html", news_list=news_list) # 注意这里form就是定义好的类

@app.route("/add", methods=["GET","POST"])
def add_news():
    """新增新闻"""
    news = Form_news()

    if news.is_submitted():
        news_toadd = News(
            title=news.title.data,
            content=news.content.data,
            news_type=news.news_type.data,
            create_at=datetime.now()
        )
        db.session.add(news_toadd)
        db.session.commit()
        flash('保存成功')
        return redirect(url_for("login1"))

    return render_template("add.html", news = news)

@app.route("/add/update<int:pk>", methods=["GET","POST"])
def update_news(pk):
    """修改新闻"""
    from NewsForm import db as thisdb
    """修改新闻"""
    new_obj = News.query.get(pk)
    if  new_obj is None:
        abort(404)

    news = Form_news(obj=new_obj)
    if news.is_submitted():
        new_obj.title = news.title.data
        new_obj.content = news.content.data
        new_obj.news_type = news.news_type.data
        new_obj.update_at = datetime.now()
        thisdb.session.add(new_obj)
        thisdb.session.commit()
        flash('修改成功')
        return redirect(url_for("login1"))

    return render_template("add.html", news = news)

@app.route("/add")
def delete_news():
    """新增页面"""
    news = Form_news()
    return render_template("add.html", news = news)


if __name__ == '__main__':
    app.run(debug=True)
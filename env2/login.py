from flask import Flask, render_template
from forms import LoginForm  # 引用

app = Flask(__name__)

@app.route("/")
def login():
    """登陆首页"""
    form = LoginForm()
    return render_template("index.html", form=form) # 注意这里

app.config["SECRET_KEY"] = 'gfbfdg' 

if __name__ == '__main__':
    app.run(debug=True)
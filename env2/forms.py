# usr/bin/env python
# coding:utf-8
# 这些都是常用的
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, RadioField, \
    TextAreaField, DateField, BooleanField, FileField
from wtforms.validators import DataRequired, ValidationError

# from wtforms.validators import passwordValid

class LoginForm(FlaskForm):

    usr = StringField('usr', validators=[DataRequired()])
    psd = PasswordField('密码',validators=[DataRequired()]
            ,render_kw={"required":"required"}) # 验证：必填
    language = RadioField('编程语言',
        choices=[('v1','python'),('v2','html')])
    code = TextAreaField('代码')
    is_checked = BooleanField("是否验证通过")
    submit = SubmitField("登陆")

class Form_news(FlaskForm):
    title = StringField(label='新闻标题' , validators=[DataRequired("请输入标题")] , description='请输入标题' ,
                        render_kw={"required":"required", "class":"form-control"}
                        )
    content = TextAreaField(label='新闻内容', validators=[DataRequired("请输入内容")], description='请输入内容',
                          render_kw={"required":"required", "class":"form-control"})
    news_type = SelectField(label="新闻类型", choices=[
        ("推荐", "推荐"), ("百家", "百家"), ("本地", "本地"), ("图片", "图片")
    ])
    submit = SubmitField("提交")
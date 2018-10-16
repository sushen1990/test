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
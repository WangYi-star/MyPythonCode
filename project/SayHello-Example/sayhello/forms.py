# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2020/5/19 11:13
# Tool ：PyCharm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length

# 提交留言的表单
class HelloForm(FlaskForm):
    body = TextAreaField('Message', validators=[DataRequired(), Length(1, 200)], id='contentcode') #定义id后，控制组件大小
    submit = SubmitField('发送')

# 登录的表单
class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(1, 20)])
    password = PasswordField("password", validators=[DataRequired(), Length(1, 20)])

# 注册的表单
class RegisterForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(1, 20)])
    password = PasswordField("password", validators=[DataRequired(), Length(1, 20)])
    againP = PasswordField("password", validators=[DataRequired(), Length(1, 20)])

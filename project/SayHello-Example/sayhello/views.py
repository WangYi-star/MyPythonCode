# coding: utf-8
# Team : Quality Management Center
# Author：Yi
# Date ：2020/5/19 11:21
# Tool ：PyCharm

from flask import redirect, url_for, render_template, request
from sayhello import app, db, bootstrap
from sayhello.forms import HelloForm, LoginForm, RegisterForm
from sayhello.model import Message, Login
from sqlalchemy import and_

# 登录
@app.route('/', methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    if request.method == 'POST':
        username = loginform.username.data
        password = loginform.password.data
        try:
            exist = db.session.query(Login).filter(Login.username == username, Login.password == password)
            user_exists = db.session.query(exist.exists()).scalar()
            if user_exists == True:                                  # 用户名和密码正确
                return redirect(url_for('home', username=username, page=int(1)))
            return '''<a type="submit" href="/">用户名或密码错误，请重新登录！</a>'''
        except Exception:
            return '''<a type="submit" href="/">登录失败，请重新登录！</a>'''
    return render_template('login.html', form=loginform)


# 注册
@app.route('/register', methods=['GET', 'POST'])
def register():
    registerform = RegisterForm()
    if request.method == 'POST':
        username = registerform.username.data
        password = registerform.password.data
        againP = registerform.againP.data
        try:
            exist = db.session.query(Login).filter(Login.username == username)
            name_exists = db.session.query(exist.exists()).scalar()
            if name_exists == True:                             # 用户名已存在
                return render_template('register.html', form=registerform, umessage='账号已存在！')
            elif againP != password:                            # 确认密码不正确
                return render_template('register.html', form=registerform, pmessage='密码错误，请再次输入！')
            else:                                               # 成功注册
                user = Login(username=username, password=password)
                db.session.add(user)
                db.session.commit()
                return '''
                <a type="submit" href="/">返回登录界面</a>
                '''
        except Exception as e:
            return render_template('register.html', form=registerform)
    return render_template('register.html', form=registerform)


# 主页
@app.route('/home', methods=['GET', 'POST'])
def home():
    helloform = HelloForm()
    username = request.args.get('username')
    page = int(request.args.get('page'))
    searchname = request.args.get('searchname')
    searchcontent = request.args.get('searchcontent')
    try:
        if helloform.validate_on_submit():                        # 发送信息
            body = helloform.body.data
            message = Message(body=body, name=username)
            db.session.add(message)
            db.session.commit()
            return redirect(url_for('home', username=username, page=1))
        if request.method == 'POST':                              # 模糊查询
            searchname = request.form.get('username')
            searchcontent = request.form.get('content')
            return redirect(url_for('home', username=username, page=1, searchcontent=searchcontent, searchname=searchname))
        if searchcontent!=None and searchname!=None:         # 模糊查询处理
            if searchname == '':
                if searchcontent != '':                      # 只根据留言内容查询
                    blogs = Message.query.filter(Message.body.like('%{}%'.format(searchcontent))).order_by(
                        Message.timestamp.desc()).paginate(page=page, per_page=10)
                else:                                        # 用户名和留言内容均为空
                    blogs = Message.query.order_by(Message.timestamp.desc()).paginate(page=page, per_page=10)
            elif searchcontent == '':                        # 只根据用户名查询
                blogs = Message.query.filter(Message.name.like('%{}%'.format(searchname))).order_by(
                    Message.timestamp.desc()).paginate(page=page, per_page=10)
            else:                                            # 根据用户名和留言内容查询
                blogs = Message.query.filter(and_(Message.body.like('%{}%'.format(searchcontent)), \
                                                  Message.name.like('%{}%'.format(searchname)))).order_by(
                    Message.timestamp.desc()).paginate(page=page, per_page=10)
            return render_template('home.html', blogs=blogs.items, pagination=blogs, form=helloform, username=username,\
                                   searchname=searchname, searchcontent=searchcontent)
    except Exception:
        return redirect(url_for('home', username=username, page=1))
    blogs = Message.query.order_by(Message.timestamp.desc()).paginate(page=page, per_page=10)
    return render_template('home.html', blogs=blogs.items, pagination=blogs, form=helloform, username=username)


# 管理我的信息
@app.route('/home/mymessage', methods=['GET', 'POST'])
def mymess():
    username = request.args.get('username')
    page = int(request.args.get('page'))
    mess_id = request.args.get('messid')
    dele = request.args.get('dele')
    try:
        if request.method == 'POST':                                    # 提交修改后的信息
            content = request.form.get('content')
            update_id = db.session.query(Message).filter(Message.id == mess_id).one()
            update_id.body = content
            db.session.commit()
            return redirect(url_for('mymess', username=username, page=page))
        if dele:                                                        # 删除该条信息
            exist = db.session.query(Message).filter(Message.id == mess_id)
            id_exists = db.session.query(exist.exists()).scalar()
            if id_exists == True:
                del_id = exist.one()
                db.session.delete(del_id)
                db.session.commit()
                return redirect(url_for('mymess', username=username, page=page))
    except:
        return redirect(url_for('mymess', username=username, page=page))
    blogs = Message.query.filter(Message.name == username).order_by \
        (Message.timestamp.desc()).paginate(page=page, per_page=10)
    return render_template('message.html', messages=blogs.items, pagination=blogs, username=username, page=page)

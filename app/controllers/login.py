#!/usr/bin/env python
#coding:utf-8
from flask import Flask, Blueprint, render_template, request, flash, session, redirect, url_for, g
from app import sms
import json
from app.models import db, User

login = Blueprint(
    'login',
    __name__
)

@login.route("/register", methods=['POST', 'GET'])
def register():
    """
    进行登录验证
    :return:
    """
    error_msg = None
    if request.method == 'GET':
        # 获取 GET 请求参数
        phone_number = request.args.get('mobile_phone_number')
        if phone_number is not None:
            if sms.send_message(phone_number):
                return render_template('form.html', error_msg=error_msg)

            else:
                error_msg = 'Failed to get the verification code!'
    elif request.method == 'POST':
        phone_number = request.form['phone']
        code = request.form['code']
        password = request.form['password']

        if code == '':
            error_msg = 'Please input the verification code!'
        elif User.query.filter(User.Tel_Number == phone_number).first():
            error_msg = u'手机号已经注册过了'
        elif sms.verify(phone_number, code):
            user_forsql = User()
            user_forsql.Password = password
            user_forsql.Tel_Number = phone_number
            db.session.add(user_forsql)
            db.session.commit()
            return redirect(url_for('printer.select'))
        else:
            error_msg = u'验证码不正确，请检查！'
            return render_template('form.html', error_msg=error_msg)
    return render_template('form.html', error_msg=error_msg)

@login.route("/clause", methods=['POST', 'GET'])
def clause():
    return render_template('clause.html')

@login.route("/login/", methods=['POST', 'GET'])
def do_login():
    if request.method == 'POST':
        tel = request.form.get('tel')
        password = request.form.get('password')
        user = User.query.filter(User.Tel_Number == tel, User.Password == password).first()
        if user:
            session['user_phone'] = user.Tel_Number
            # session['user_loged'] = 1
            g.current_userphone = session['user_phone']
            g.current_user = user
            print "Log in OK"
            flag = 1
            return redirect('/select?flag=2')
        else:
            print "Log in Failed"
            flag = 2
            return redirect('/select?flag=2')


@login.route("/logout", methods=['GET'])
def logout():
    session.pop('user_phone', None)
    g.current_userphone = json.dumps(None)
    return render_template('index.html')



# @login.route("/test", methods=['POST', 'GET'])
# def logins():
#     """
#     进行登录验证
#     :return:
#     """
#     error_msg = None
#     if request.method == 'GET':
#         # 获取 GET 请求参数
#         phone_number = request.args.get('mobile_phone_number')
#         if phone_number is not None:
#             if sms.send_message(phone_number):
#                 return render_template('login.html')
#             else:
#                 error_msg = 'Failed to get the verification code!'
#                 print error_msg
#                 flash("failed", category="failed")
#
#     elif request.method == 'POST':
#         phone_number = request.form['phone']
#         code = request.form['code']
#         if code == '':
#             error_msg = 'Please input the verification code!'
#         elif sms.verify(phone_number, code):
#             return redirect(url_for('success'))
#         else:
#             error_msg = 'Your code is wrong, please check again!'
#     return render_template('login.html', error_msg=error_msg)

@login.route("/success")
def success():
    return render_template('success.html')


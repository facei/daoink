#!/usr/bin/env python
#coding:utf-8
from flask import Flask, Blueprint, render_template, request, flash, session, redirect, url_for, g
from app import sms

login = Blueprint(
    'login',
    __name__
)

@login.route("/login", methods=['POST', 'GET'])
def do_login():
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
                print error_msg
    elif request.method == 'POST':
        phone_number = request.form['phone']
        code = request.form['code']
        if code == '':
            error_msg = 'Please input the verification code!'
        elif sms.verify(phone_number, code):
            return redirect(url_for('success'))
        else:
            error_msg = 'Your code is wrong, please check again!'
            return render_template('form.html', error_msg=error_msg)
    return render_template('form.html', error_msg=error_msg)

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


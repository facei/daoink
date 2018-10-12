# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from flask import Flask, redirect, url_for, render_template, session, g, jsonify, request
from config import DevConfig
from models import db, User, Order
from controllers.printer import printer
from controllers.login import login
import datetime, json

app = Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)
# app.permanent_session_lifetime = datetime.timedelta(seconds=10*60)          #设置sission过期时间为10min

# 自定义jinja过滤器
def time_format(l):
    return str(l)[:-7]
app.add_template_filter(time_format, 'format_time')


@app.route('/')
def index():
    if g.current_user != None:
        user_order = Order.query.filter(Order.User_Id == g.current_user.Id).all()
        lenth = len(user_order)
        return render_template('index.html', user_order=user_order, lenth=lenth)
    else:
        user_order = None
        lenth = 0
        return render_template('index.html', user_order=user_order, lenth=lenth)


@app.before_request
def check_user():
    if 'user_phone' in session:
        g.current_userphone = session['user_phone']
        user = User.query.filter(User.Tel_Number == g.current_userphone).first()
        g.current_user = user

    else:
        g.current_userphone = json.dumps(None)
        g.current_user = None




app.register_blueprint(printer)
app.register_blueprint(login)

if __name__ == '__main__':
    app.run(host='192.168.3.5', port=80)
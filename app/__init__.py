# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from flask import Flask, redirect, url_for, render_template, session, g, jsonify, request
from config import DevConfig
# # from models import db
from controllers.printer import printer
from controllers.login import login
import datetime

app = Flask(__name__)
app.config.from_object(DevConfig)

app.permanent_session_lifetime = datetime.timedelta(seconds=5*60)          #设置sission过期时间为5min

# 自定义jinja过滤器
def time_format(l):
    return str(l)[:-7]
app.add_template_filter(time_format, 'format_time')


@app.route('/')
def index():
    return render_template('index.html')

@app.before_request
def check_user():
    if 'user_id' in session:
        g.current_user = User.query.filter_by(Id=session['user_id']).one()

    else:
        g.current_user = None



app.register_blueprint(printer)
app.register_blueprint(login)

if __name__ == '__main__':
    app.run(host='192.168.3.5', port=80)
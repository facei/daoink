#!/usr/bin/env python
#coding:utf-8
from flask import Flask, Blueprint, render_template, request, flash, session, redirect, url_for, g
import datetime, os
from app.models import db, User, Order
from werkzeug.utils import secure_filename
printer = Blueprint(
    'printer',
    __name__
)

@printer.route('/select', methods=['GET', 'POST'])
def select():
    global datetimes
    global now
    datetimes = datetime.datetime.now()
    now = str(datetimes.year)+"-"+str(datetimes.month)+"-"+str(datetimes.day)+"_"+str(datetimes.hour)+":"+str(datetimes.minute)
    if request.method == 'POST':
        printfile = request.files['uploadfile']         # 文件
        place = request.form.get("place")               # 打印点
        copies = request.form.get("copies")             # 份数
        direction = request.form.get("direction")       # 排版方向
        colour = request.form.get("colour")             # 彩色或黑白
        paper_size = request.form.get("paper_size")     # 纸张大小
        print_way = request.form.get("print_way")       # 单双面
        time_way = request.form.get("time_way")         # 预约或自动排队
        cost = 0.2

        filename = printfile.filename
        index_point = filename.index(".")
        new_filename = str(g.current_user.Tel_Number)+"_" + now + filename[index_point:]
        # basepath = os.path.dirname(__file__)
        basepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        print basepath
        upload_path = os.path.join(basepath, 'static/Upload_Files', secure_filename(new_filename))
        print upload_path
        printfile.save(upload_path)


        data = {"printfile": printfile, "new_filename": new_filename, "place": place, "copies": copies, "direction": direction, "colour": colour, "paper_size": paper_size,
                "print_way": print_way, "time_way": time_way, "cost": cost}

        return render_template('confirm.html', data=data)


    return render_template('select.html', now=now)


@printer.route('/confirm', methods=['GET', 'POST'])
def confirm():
    global result
    result = 0
    cost = request.form.get("cost")
    user = User.query.filter(User.Tel_Number == g.current_userphone).first()
    cost = float(cost)
    if cost <= user.Money:
        result = 1
        return render_template("result.html", result=result)
    else:
        return render_template("result.html", result=result)

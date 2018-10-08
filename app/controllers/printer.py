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
    now = str(datetimes.year)+"-"+str(datetimes.month)+"-"+str(datetimes.day)+"_"+str(datetimes.hour)+"-"+str(datetimes.minute)+"-"+str(datetimes.second)
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
        upload_path = os.path.join(basepath, 'static/Upload_Files', secure_filename(new_filename))
        printfile.save(upload_path)


        data = {"printfile": printfile, "new_filename": new_filename, "place": place, "copies": copies, "direction": direction, "colour": colour, "paper_size": paper_size,
                "print_way": print_way, "time_way": time_way, "cost": cost}


        return render_template('confirm.html', data=data)
    flag = request.args.get('flag')
    print flag
    if flag == '2':
        return render_template('select.html', now=now, flag=flag)
    elif flag == '1':
        return render_template('select.html', now=now, flag=flag)
    else:
        print "mad"
        return render_template('select.html', now=now)


@printer.route('/confirm', methods=['GET', 'POST'])
def confirm():
    global result
    result = 0
    cost = request.form.get("cost")
    user = User.query.filter(User.Tel_Number == g.current_userphone).first()
    cost = float(cost)
    if cost <= user.Money:

        order_forsql = Order()
        order_forsql.User_Id = user.Id
        order_forsql.File_Dir = request.form.get("filename")
        order_forsql.Time_Way = request.form.get("time_way")
        order_forsql.Print_Place = request.form.get("place")
        order_forsql.Print_Copies = request.form.get("copies")
        order_forsql.Print_Direction = request.form.get("direction")
        order_forsql.Print_Colour = request.form.get("colour")
        order_forsql.Print_size = request.form.get("paper_size")
        order_forsql.Print_way = request.form.get("print_way")
        order_forsql.Print_Money = request.form.get("cost")
        order_forsql.Print_Status = 1

        db.session.add(order_forsql)
        db.session.commit()

        user.Money = round(user.Money - float(request.form.get("cost")), 1)
        db.session.add(user)
        db.session.commit()

        result = 1
        return render_template("result.html", result=result)
    else:
        return render_template("result.html", result=result)

@printer.route('/result', methods=['GET', 'POST'])
def result():
    return 'ok'
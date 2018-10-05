# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
import datetime, os, time

#数据模型部分
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'  #表名字默认是类名字的小写版本(如果没有此语句)

    Id = db.Column(db.Integer(), primary_key=True)
    Tel_Number = db.Column(db.String(255), nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    Money = db.Column(db.Float(), default=0.5)
    Register_Date = db.Column(db.DateTime, default=datetime.datetime.now)




class Order(db.Model):
    __tablename__ = 'Order'

    Id = db.Column(db.Integer(), primary_key=True)
    File_Dir = db.Column(db.String(255), nullable=False)
    Born_Date = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
    Time_Way = db.Column(db.Integer())
    Print_Date = db.Column(db.DateTime)
    Print_Place = db.Column(db.String(255), nullable=False)
    Print_pages = db.Column(db.Integer())                      # 每份页数
    Print_Copies = db.Column(db.Integer())                     # 份数
    Print_Direction = db.Column(db.String(255), nullable=False)
    Print_Colour = db.Column(db.String(255), nullable=False)
    Print_size = db.Column(db.String(255), nullable=False)
    Print_way = db.Column(db.String(255), nullable=False)
    Print_Money = db.Column(db.Float())                         # 订单价格
    Print_Status = db.Column(db.Integer(), default=0)          # 订单状态，0 未支付, 1 已经打印,2 未打印


    User_Id = db.Column(db.Integer(), db.ForeignKey('User.Id'), nullable=False)
    user = db.relationship('User', foreign_keys='Order.User_Id')





#
# class Mession(db.Model):
#     __tablename__ = 'Mession'
#
#     Id = db.Column(db.Integer(), primary_key=True)
#     Title = db.Column(db.String(255), nullable=False)
#     Details = db.Column(db.String(255), nullable=False)
#     Picture_Name = db.Column(db.String(255))
#
#
#     Born_Date = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
#     Dead_Date = db.Column(db.DateTime, nullable=False)
#     Got_Date = db.Column(db.DateTime)                                                     # 接单的时间
#     Finish_Date = db.Column(db.DateTime)
#     Finish = db.Column(db.Integer(), nullable=False)
#
#     Maker_Id = db.Column(db.Integer(), db.ForeignKey('User.Id'), nullable=False)         # 发单用户的Id
#     Worker_Id = db.Column(db.Integer(), db.ForeignKey('User.Id'))                          # 接单用户的Id
#
#     Maker = db.relationship('User', foreign_keys='Mession.Maker_Id')
#     Worker = db.relationship('User', foreign_keys='Mession.Worker_Id')
#

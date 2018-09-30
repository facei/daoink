# # -*- coding: utf-8 -*-
# from flask_sqlalchemy import SQLAlchemy
# import datetime, os, time
#
# #数据模型部分
# db = SQLAlchemy()
#
# class User(db.Model):
#     __tablename__ = 'User'  #表名字默认是类名字的小写版本(如果没有此语句)
#
#     Id = db.Column(db.Integer(), primary_key=True)
#     Password = db.Column(db.String(255))
#     Name = db.Column(db.String(255))
#     Gender = db.Column(db.Integer())
#     Birth = db.Column(db.Integer())
#     Position = db.Column(db.Integer())
#     Email = db.Column(db.String(255))
#     Tel_Number = db.Column(db.String(255))
#     Register_Date = db.Column(db.DateTime, default=datetime.datetime.now)
#
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

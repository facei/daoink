#!/usr/bin/env python
#coding:utf-8
from flask import Flask, Blueprint, render_template, request, flash, session, redirect, url_for, g
printer = Blueprint(
    'print',
    __name__
)

@printer.route('/select', methods=['GET', 'POST'])
def select():
    return render_template('select.html')



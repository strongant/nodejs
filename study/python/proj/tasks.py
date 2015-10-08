# _*_coding: UTF-8_*_
__author__ = 'bwh'

from __future__ import absolute_import
from testcelery import app


@app.task
def add(x,y):
    return x+y


@app.task
def mul(x,y):
    return x*y

@app.task
def xsum(numbers):
    return sum(numbers)


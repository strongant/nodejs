# _*_coding: UTF-8_*_
__author__ = 'bwh'

def f(x):
    return x*x
# r = map(f,[1,2,3,4,5,6,7,8,9])
# arr = list(r)
# print arr

#map将数字转换为字符串
# arr = list(map(str,[1,2,3,4,5,6,7,8,9]))
# print arr

#使用raduce进行求和运算
from functools import reduce
# def add(x,y):
#     return x+y
# count = reduce(add,[1,2,3,4,5,6])
# count = sum([1,2,3,4,5,6])
# print count


def fn(x,y):
    return x*10+y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

result = reduce(fn,map(char2num,'13579'))
print result

#map后的值
r = map(char2num,'13579');
l = list(r)
print  l



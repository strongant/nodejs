# _*_coding: UTF-8_*_
__author__ = 'bwh'
import demjson

data = [{'a':1,'b':2,'c':3}]

json = demjson.encode(data)
print json


json = '{"a":1,"b":2,"c":3}'

text = demjson.decode(json)
print text
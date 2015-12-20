# _*_coding: UTF-8_*_
__author__ = 'bwh'

try:
    fh = open("ceshi","r")
    fh.write("THis is my test file for exception")
    print "写入文件成功"
    fh.close()
except IOError:
    print "Error:can't find file"



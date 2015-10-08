# _*_coding: UTF-8_*_
__author__ = 'bwh'

#导入support模块
import support


support.print_func("ＺARA")

#使用ｆｒｏｍ进行导入
from support import print_func
print_func("测试")


#dir()函数
import math
cotent = dir(math)

print(cotent)

reload(support)

def Pots():
    print "I'm Pots Phone"
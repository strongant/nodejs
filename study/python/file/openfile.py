# _*_coding: UTF-8_*_
__author__ = 'bwh'

#打开文件
#fo = open("test.txt","r+")


#向空白文件写入内容
# fo = open("test.txt","r+")
# fo.write("Python is a great language.\nYeah its great!!\n")
# fo.close()


'''
print 'filename:',fo.name;
print 'closed or not:',fo.closed
print 'opening mode:',fo.mode
print 'softspace flag:',fo.softspace

#向空白文件写入内容
fo.write("Python is a great language.\nYeah its great!!\n")
fo.close()


fo = open("test.txt","r+")
#读取文件
str = fo.read(100);
print "文件内容:",str
#关闭打开的文件
fo.close()
'''

# poition = fo.tell()
# print "curent file poistion : ",poition

# poition = fo.seek(0,0);
# str = fo.read(10);
# print "seek content is :",str
# #关闭打开的文件
# fo.close()

import os
#重命名文件
# os.rename("test.txt","text1.txt")
# os.remove("text1.txt")

#创建文件夹
#os.mkdir()
#删除文件夹
#os.rmdir("dir")

#显示当前目录
print os.getcwd()












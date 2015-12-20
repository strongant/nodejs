# _*_coding: UTF-8_*_
__author__ = 'bwh'
import time;

ticks = time.time()
print ticks

#获取当前时间
ticks = time.localtime(time.time())
print 'localtime:',ticks


#获取格式化时间
localtime = time.asctime(time.localtime(time.time()))
print 'Local current time:',localtime
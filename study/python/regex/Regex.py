# _*_coding: UTF-8_*_
__author__ = 'bwh'
import re

# print(re.match("www","www.runoob.com").span())  #从起始位置匹配
# print(re.match("com","www.runoob.com"))  #不在起始位置匹配






#正则匹配
line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)


if matchObj:
    print "matchObj.group():",matchObj.group()
    print "matchObj.group(1):",matchObj.group(1)
    print "matchObj.group(2):",matchObj.group(2)
else:
    print "NO Match!!"

#正则查找
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配






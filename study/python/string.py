# _*_coding: UTF-8_*_
__author__ = 'bwh'


str = 'abcdefg'
#此方法将字符串中的小写字母大写
str = str.capitalize()
print str

#str.center　向两边添加数组
str = "this is string"
print "str.center(40,'a'):",str.center(20,'a')

#count()方法的实例,统计某个字符在字符串中出现了多少次
str = "this is string example"

sub = "i"
print "str.count(sub,4,40):",str.count(sub,0,len(str))
sub = "e"
print "str.count(sub):",str.count(sub)


#decode 方法
str = "this is string example"
str = str.encode('base64','strict')

print str
print 'decode:' + str.decode('base64','strict')








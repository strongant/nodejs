# _*_coding: UTF-8_*_
__author__ = 'bwh'

a = 21
b = 10
c = 0

c = a**b
print "a的１０次方",c

c = a//b
print "整除，只取整数位",c

a = 10
b = 20
c = 0
if (a and b):
    print "a and b true"
else:
    print "a or b is not true"


if (a or b):
    print "a or b is  true"
else:
    print 'a is true not b is true'

a = 0
if(a and b):
    print 'a and b is true'
else:
    print 'a and b is not true'

if (a or b):
    print "a or b is  true"
else:
    print 'a is true not b is true'



if not(a and b):
    print 'not and b is true'
else:
    print "a and b are false"

#成员运算符
a = 10
b = 20
list = [1,2,3,4,5]

if (a in list):
    print 'a is in list'
else:
    print 'a is not in list'

if (b not in list):
    print 'b is not in list'
else:
    print 'false'

a = 2
if (a in list):
    print 'true'
else:
    print 'false'

a = 20
b = 20

#is 判断身份
if (a is b):
    print 'a is b'
else:
    print 'a is not b'

#id 判断身份
if (id(a) == id(b)):
    print 'a id b is true'
else:
    print 'a id b is not true'




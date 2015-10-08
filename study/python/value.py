# _*_coding: UTF-8_*_
__author__ = 'bwh'

counter = 100 #整型
miles = 1000.0 #浮点型
name = "John";

print(counter)
print(miles)
print(name)

#多个变量赋值
a=b=c=1
print(a,b,c)

a,b,c=1,2, "john"
print(a,b,c)


#字符串
s="a1a2```an"
print(s)

str = 'Hello World';

print str
print str[0] #输出字符串中的第一个字符
print str[2:5] #取出字符串中的第三个至第五个之间的字符
print str[2:] #取出第三个字符之前的字符串
print str * 2 #输出字符串两次
print str + "TEST" #输出连接的字符串



#Python　列表
print '\n\n列表'
list = ['abcd',786,2.23,'john',70.2]
tinylist = [123,'john']

print list #输出完整列表
print list[0] #输出第一个元素
print list[1:3] #输出第二个到第三个元素
print list[2:] #输出从第三个开始到末尾的所有元素
print tinylist * 2 #输出列表两次
print list + tinylist #打印组合的列表

#Python元组
print '\n\n元组'
tuple = ('abcd',786,2.23,'john',70.2)
tinytuple = (123,'john')


#元组和列表的区别是元组是只读的，列表可以动态赋值
print '\n\n元组和list区别'

tuplea = ( 'abcd', 786, 2.23)
lista = ['abcd',786,2.23,'john',70.2]

#tuplea[2] = 100 #元组只读不允许更新
lista[2] = 1000 #列表是合法应用


print tuplea
print lista

#Python元字典

dict = {}
dict['one'] = 'This is a one'
dict[2] = 'This is a two'

tinydict = {'name':'john','code':'6734','dept':'sales'}


print dict['one']
print dict[2]
print tinydict
print tinydict.keys() #输出所有键
print tinydict.values() #输出所有值



















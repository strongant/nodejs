# _*_coding: UTF-8_*_
__author__ = 'bwh'

def printtime(str):
    "打印传入的字符串"
    print str
    return

printtime("调用")

#可写函数
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1,2,3,4]);
    print '函数内取值',mylist
    return

mylist = [10,20,30];
changeme(mylist)
print "函数外取值:",mylist


#命名参数
def printme(str):
    print str;
    return;

printme(str = "My String")

def printinfo(name, age = 35):
    print "name:",name;
    print "age",age
    return;

printinfo(age=50,name="miki")
printinfo("aaa")


#可写函数说明
def printinfowrite(arg1,*vartuple):
    print "输出:"
    print "第一个参数:",arg1
    for var in vartuple:
        print var
    return;

printinfowrite(10);
printinfowrite(70,60,80,90)


#lambda
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print "相加后的值为 : ", sum( 10, 20 )

sum = lambda arg1, arg2: arg1 + arg2;
print "相加后的值为:",sum(10,20)
print "相加后的值为:",sum(20,20)
# 赋值
number = 42
options = true

#条件
number = -42 if opposite

#函数
square = (x)->x*x

#数组
list = [1,2,3,4]

#对象
math =
  root:Math.sqrt
  square:square
  cube:(x)->x * square x

#Splats
race = (winner,runners...)->
  print winner,runners

#存在性
alert "I knew it!" if elvls?

#数组
cubes = (math.cube num for num in list)



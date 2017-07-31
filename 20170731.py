#python教程
#函数的参数

#当你在编写一个程序时，执行语句部分思路还没有完成，这时你可以用pass语句来占位，也可以当做是一个标记，是要过后来完成的代码。比如下面这样：
#>>>def iplaypython():
#>>>       pass
#定义一个函数iplaypython，但函数体部分暂时还没有完成，又不能空着不写内容，因此可以用pass来替代占个位置。

def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print(" name",name,'age:',age,'other:',kw)

person('lk',24,city="重庆",addr="重庆",zipid=123456)

#output :
# name lk age: 24 other: {'addr': '重庆', 'city': '重庆', 'zipid': 123456}
#限制关键字参数的名字 用命名关键字参数 例如 该例子只接受city和job作为其关键字
def person(name,age,*,city,job):
    print(name,age,city,job)
#必须给出参数名称，如果没有传入参数名 调用将出错
person("dcc",21,city="四川",job="it")
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：
# 必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a,b,c=0,*args,**kw):
    print("a = ",a,'b=',b,'c=',c,'args = ',args,'kw=',kw)

def f2(a,b,c=0,*,d, **kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

#参数组合调用
f1(1,2)
f1(1,2,3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=3)
f2(1,2,d=99,ext=None)
#a =  1 b= 2 c= 0 args =  () kw= {}
#a =  1 b= 2 c= 3 args =  () kw= {}
#a =  1 b= 2 c= 3 args =  ('a', 'b') kw= {}
#a =  1 b= 2 c= 3 args =  ('a', 'b') kw= {'x': 3}
#a= 1 b= 2 c= 0 d= 99 kw= {'ext': None}
args=(1,2,3,4)#tuple
kw={'d':99,'x':'$'}#dict

f1(*args,**kw)
args=(1,2,3)
kw={'d':88,'x':'#'}
f2(*args,**kw)
#a =  1 b= 2 c= 3 args =  (4,) kw= {'x': '$', 'd': 99}
#a= 1 b= 2 c= 3 d= 88 kw= {'x': '#'}
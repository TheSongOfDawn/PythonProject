#获取对象信息
#Python 中不支持方法重载！！！！！！！
#批量注释 ctrl+/
#type()返回的是对应的class类型
import types
print(type(123))
print(type(abs))
print(type(123)==type(456))
print(type(123)==int)
print(type('abc')==type('132'))
print(type('abc')==str)

def fn():
    pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x  in range(10)))==types.GeneratorType)


#isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上
class Animal:
    pass
class Dog(Animal):
    pass

d=Dog()
a=Animal()
print("isinstance isinstance(a,Animal)",isinstance(a,Animal))

#获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，
print(dir(Dog))
print(dir('abc'))
#配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状
class MyObject(object):
    def __init__(self):
        self.x=9

obj=MyObject()
print("有属性X吗？",hasattr(obj,'x'))
print("有属性y吗？",hasattr(obj,'y'))
setattr(obj,'y','10')
print("有属性y吗？",hasattr(obj,'y'))
print(getattr(obj,'y'))

print(obj.y)

#使用__slots__

#class Stu(object):
#     __slots__=('name','age')

#s=Stu()
#s.name='dc'#绑定属性 'name'
#s.age=99#绑定属性 age
#s.score=100
#output:
# s.score=100 AttributeError: 'Stu' object has no attribute 'score'
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

class Stu(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must be an integer!")
        if value<0 or value>100 :
            raise ValueError("score must between 0~100")
        self._score=value
    def __init__(self,name):
        self.name=name
    def __init__(self):
        pass

# 一旦引发了raise错误 后面的语句就无法执行
s=Stu()
s.score=100
#s.score=1000 该句执行会出错
#在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
#__slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return ('student object(name: %s'%(self.name))
    __repr__=__str__

    def __getattr__(self, attr):
        if attr=='age':
            return lambda :25
        raise  AttributeError("\Student\" object has no attribute \' %s\'"%attr)
    def __call__(self):
        print("my Name is %s."%self.name)

    #def __init__(self): 类似于构造方法 但是不能重载
     #   pass
#未定义__str__时输出
#<__main__.Student object at 0x0000000000DE7CC0>
print(Student("michael"))
s=Student("michael")
s()
#判断一个对象/函数能否被调用
callable(max)
#如果在命令行直接输出s 则还是未定义str的那种输出
#这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

#解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
#__iter__
#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1 #初始化两个计数器
    def __iter__(self):
        return self #实例本身是迭代自己 故返回自己

    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>100000:
            raise StopIteration()
        return self.a
    def __getitem__(self, item):
        a,b=1,1
        for x in range(item):
            a,b=b,a+b
        return a

for n in Fib():
    print(n)
f=Fib() #相当于生成了一个list
print(f[100])
#getitem 能够使类看起来能像list 那样按照下标取出元素 需要实现 __getitem__()方法

#__getattr__ 在没有找到属性的情况下 才调用__getattr__ 已有的属性不会在__getattr__中找
#实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段可以针对完全动态的情况作调用。
#一个对象实例可以有自己的属性和方法 当我们调用实例方法时，我们可以用instance.method()来调用也可以直接用istance()这种方法调用

# -*- coding: utf-8 -*-
#高阶函数
#map()map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
#output:[1, 4, 9, 16, 25, 36, 49, 64, 81]

#reducereduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f,[x1,x2,x3,...])=f(f(f(x1,x2),x3),x4)
#exp 序列求和:
from functools import reduce
def fn(x,y):
    return x*10+y
print(reduce(fn,[1,3,5,7,9]))
#output:13579

#filter
#和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n%2==1

#如果不加list
#output：<filter object at 0x0000000000DD84A8>
#加一个list
#[1, 3, 5, 7, 9, 11, 13, 45, 15]
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10,11,12,13,45,15])))
#sorted 排序算法
#sorted()函数就可以对list进行排序 它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
# y指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
#sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
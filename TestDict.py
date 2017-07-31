#测试单元模块
import unittest
from mydict import Dict
#self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等
#以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
#测试方法都会运行 互不影响
#可以在单元测试中编写两个特殊的方法 setUp() tearDown()方法
#输出显示每个方法测试之前都调用了setUp方法 每个方法测试之后都调用了tearDown方法
#unittest参考:https://docs.python.org/2/library/unittest.html

#学习了测试类以后 要将自动化测试程序写规范
class TestDict(unittest.TestCase):
    def test_init(self):
        d=Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))
    def test_key(self):
        d=Dict()
        d['key']='value'
        self.assertEqual(d.key,'value')

    def test_attr(self):
        d=Dict()
        d.key='value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')

    def test_keyerror(self):
        d=Dict()
        with self.assertRaises(KeyError):
            value=d['empty']

    def test_atterror(self):
        d=Dict()
        with self.asserRaisers(AttributeError):
            value=d.empty
    def test_myOo(self):
        print("这是一个空的测试方法")

    def setUp(self):
        print("setUp()方法")
    def tearDown(self):
        print("tearDown()方法")


if __name__=='__main__':
    unittest.main()


#ErroAndIO.py
#try:
#...
#finally 有finally就会自动执行

try:
    print('try...')
    r=10/int('2')
    print('result:',r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:
    print("no ERROR!")
finally:
    print("finally...")
print("END")

#断言 可以用print 辅助查看的地方可以用断言 assert来替代
def foo(s):
    n=int(s)
    assert n!=0,'n is zero!'
    return 10/n

#foo('0')
#assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
#如果断言失败，assert语句本身就会抛出AssertionError：

#启动python解释器可以用 -0来关闭assert

#将print()替换为logging
# import logging
# logging.basicConfig(level=logging.INFO)
# s='0'
# n=int(s)
# logging.info('n=%d'%n)
# print(10/n)
#跳过了后面的文档测试！

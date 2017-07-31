# #try:
# #...
# #finally 有finally就会自动执行
#
# try:
#     print('try...')
#     r=10/int('2')
#     print('result:',r)
# except ValueError as e:
#     print('ValueError:',e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:',e)
# else:
#     print("no ERROR!")
# finally:
#     print("finally...")
# print("END")
#
# #断言 可以用print 辅助查看的地方可以用断言 assert来替代
# def foo(s):
#     n=int(s)
#     assert n!=0,'n is zero!'
#     return 10/n
#
# #foo('0')
# #assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
# #如果断言失败，assert语句本身就会抛出AssertionError：
#
# #启动python解释器可以用 -0来关闭assert
#
# #将print()替换为logging
# # import logging
# # logging.basicConfig(level=logging.INFO)
# # s='0'
# # n=int(s)
# # logging.info('n=%d'%n)
# # print(10/n)
#
# 文件读写
# 传入文件名称和标识符 r 表示读
# 如果文件不存在open函数就会抛出一个IOErro错误 并给出错误代码和详细的信息告诉你文件不存在
# 基础操作
# f=open("D:\\pycodes\\1.txt",'r')
# read()方法可以一次性调用文件的全部内容到内存中 用一个str对象表示
# f.read()
# f.close()
# Python引入了with语句来自动帮我们调用close()方法
# with open("D:\\pycodes\\1.txt",'r') as f:
#     print(f.read())
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，
# 反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
# for line in f.readline():
#     print(line.strip())#去掉末尾的\n遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
#
#  open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
#
#
# 写文件 传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
# with open('/Users/michael/test.txt', 'w') as f:
#     f.write('Hello, world!'
# 要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。


## StringIO 在内存中读写str
from io import StringIO
f=StringIO()
f.write("你好！")
#getvalue()方法用于获得写入后的str。
print(f.getvalue())#hello
#读取stringio可以用一个str初始化StringIO，然后，像读文件一样读取

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
#
# Hello!
# Hi!
# Goodbye!

#BytesIO
#
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
#
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
#
# >>> from io import BytesIO
# >>> f = BytesIO()
# >>> f.write('中文'.encode('utf-8'))
# 6
# >>> print(f.getvalue())
# b'\xe4\xb8\xad\xe6\x96\x87'
# 请注意，写入的不是str，而是经过UTF-8编码的bytes。
#
# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
#
# >>> from io import BytesIO
# >>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# >>> f.read()
# b'\xe4\xb8\xad\xe6\x96\x87'


#操作文件和目录
#  import os
# >>> os.name # 操作系统类型
# 'posix'
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
#
# >>> os.environ
# environ({'VERSIONER_PYTHON_PREFER_32_BIT': 'no', 'TERM_PROGRAM_VERSION': '326', 'LOGNAME': 'michael', 'USER': 'michael', 'PATH': '/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin', ...})
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
#
# >>> os.environ.get('PATH')
# '/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin'
# >>> os.environ.get('x', 'default')
# 'default'
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
#
# # 查看当前目录的绝对路径:
# >>> os.path.abspath('.')
# '/Users/michael'
# # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# >>> os.path.join('/Users/michael', 'testdir')
# '/Users/michael/testdir'
# # 然后创建一个目录:
# >>> os.mkdir('/Users/michael/testdir')
# # 删掉一个目录:
# >>> os.rmdir('/Users/michael/testdir')
#把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
#同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

# >>> os.path.split('/Users/michael/testdir/file.txt')
# ('/Users/michael/testdir', 'file.txt')
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
#
# >>> os.path.splitext('/path/to/file.txt')
# ('/path/to/file', '.txt')
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
#
# 文件操作使用下面的函数。假定当前目录下有一个test.txt文件：
#
# # 对文件重命名:
# >>> os.rename('test.txt', 'test.py')
# # 删掉文件:
# >>> os.remove('test.py')
# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。
#
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
#
# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
#
# >>> [x for x in os.listdir('.') if os.path.isdir(x)]
# ['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]
# 要列出所有的.py文件，也只需一行代码：
#
# >>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
# ['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']
#我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
#序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# Python提供了pickle模块来实现序列化。
#
# 首先，我们尝试把一个对象序列化并写入文件：
#
# >>> import pickle
# >>> d = dict(name='Bob', age=20, score=88)
# >>> pickle.dumps(d)
# b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
#
# >>> f = open('dump.txt', 'wb')
# >>> pickle.dump(d, f)
# >>> f.close()
# 看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息。
#
# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象：
#
# >>> f = open('dump.txt', 'rb')
# >>> d = pickle.load(f)
# >>> f.close()
# >>> d
# {'age': 20, 'score': 88, 'name': 'Bob'}


#json 编码格式是 utf-8
#内置json模块
import json
d=dict(name='dc',age='19',score=20)
json.dumps(d)
#output:{'age': 20, 'score': 88, 'name': 'Bob'}
#进阶
#python内的dict对象可以直接序列化为json的{}
#默认情况下 dumps()不知道如何将student实例变为一个json的{}
#可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
# def student2Dicdt(std):
#     return{
#         'name':std.name,
#         ...
#     }
#Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
#print(json.dumps(s, default=student2dict))
#偷懒做法
#print(json.dumps(s, default=lambda obj: obj.__dict__))
class teacher(object):
    def __init__(self):
        self.name='dc'
        self.age=19
        self.score=60
s = teacher()
#自己覆盖了__dict__()该方法，这里调用就要加()
#没有覆盖就不要加()
print(json.dumps(s, default=lambda object: object.__dict__))

#反序列化
# def dict2student(d):
#     return Student(d['name'], d['age'], d['score'])
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# >>> print(json.loads(json_str, object_hook=dict2student))
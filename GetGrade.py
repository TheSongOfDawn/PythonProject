# -*- coding: utf-8 -*-
#重庆科技学院 做了登陆 这个版本还没有做成绩的排版
import requests
url='http://web.cqust.edu.cn:9080/userPasswordValidate.portal'
s=requests.session()
s.get(url)
cookie_value= ''
for x in s.cookies:
    if x.name == 'JSESSIONID':
        cookie_value = x.value
        break
head= {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':181,
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':cookie_value,
'Host':'web.cqust.edu.cn',
'Origin':'http://web.cqust.edu.cn',
'Referer':'http://web.cqust.edu.cn/',
'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}
Login={'Login.Token1':'usernam',
	'Login.Token2':'like200376',
    'goto':'http://web.cqust.edu.cn:9080/loginSuccess.portal',
    'gotoOnFail':'http://web.cqust.edu.cn:9080/loginFailure.portal'}
s.post(url,data=Login,headers=head)
grade_url = "http://jwnew.cqust.edu.cn/eams/teach/grade/course/person!historyCourseGrade.action?projectType=MAJOR"
grade_result=s.get(grade_url).content
try:
    with open('/home/ubuntu/codes/file'+'grade.html','wb') as write_grade:
        write_grade.write(grade_result)
except IOError:
 print("IO Error/n")
finally:
    write_grade.close
print grade_result

# -*- coding: utf-8 -*-
__author__ = 'lk'
import requests
import json
url='http://wthrcdn.etouch.cn/weather_mini?city=%s'
cityname=raw_input("请输入你想查哪个城市的天气\n")
try:
    url=url%cityname
    r=requests.get(url)
    data=r.json()
    wendu=data['data']['wendu']
    print '当前温度:'+wendu.encode('utf-8')
    forecast=data['data']['forecast']
    for tianqi in forecast:
        print tianqi['date']
        print tianqi['type']
        print tianqi['high']
        print tianqi['low']
        fengxiang='风向:'+tianqi['fengxiang'].encode('utf-8')
        print fengxiang
        fengli='风力:'+tianqi['fengli'].encode('utf-8')
        print fengli+'\n'
except:
    print '查询失败'

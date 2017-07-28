# -*- coding: utf-8 -*-

#微信抓取好友信息 版本0.5
import itchat
import jieba
import re
from pyecharts import Bar,Geo,Pie
from pyecharts import WordCloud

class mywechat(object):
    def __init__(self):
        # 登录
        itchat.login()
    def get_friends_Signature(self):
        # 获取好友个性签名
        tList=[]
        #第0个是自己
        friends=itchat.get_friends(update=True)[1:]
        for i in friends:
            #获取个性签名
            signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
            rep = re.compile("1f\d.+")
            signature = rep.sub("", signature)
            tList.append(signature)
        for s in tList:
            print(s)

    def get_friends_city(self):
        friends = itchat.get_friends(update=True)[0:]
        citys={}
        nullcity=0
        # 给citys键值对赋值 不然会出错
        for i in friends:
            #获取好友所在城市
            city = i["City"]
            if city!="":
                citys[city]=0
            else:
                nullcity+=1

        for i in friends:
            #获取好友所在城市
            city = i["City"]
            if city!="":
                citys[city]+=1
        #bar = Bar(u'%s的微信好友所在城市' % (friends[0]['NickName']), 'from WeChat')
        #转化为list
        #citys_key= list( citys.keys())
        #citys_value=list(citys.values())
        #bar.add("城市", citys_key,citys_value)
        #bar.show_config()
        #bar.render(r"d:\pic\mywechat_friends_citys.html")

        #citys_key= list( citys.keys())
        #citys_value=list(citys.values())
        geo =Geo(u'%s的微信好友所在城市' % (friends[0]['NickName']),'from WeChat', title_color="#fff", title_pos="center",
                width=1200, height=600, background_color='#404a59')
        attr, value = geo.cast(citys)
        geo.add("", attr, value, visual_range=[0, 7], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
        geo.show_config()
        #写到d盘的pic文件夹
        geo.render(r"d:\pic\my_friends_citys.html")

    def get_friends_sex(self):
        # 获取好友列表
        friends = itchat.get_friends(update=True)[0:]
        print(friends[0])
        # 初始化计数器
        male = female = other = 0
        # 第一位是自己
        # 1 表示男性 2 女性
        for i in friends[1:]:
            sex = i["Sex"]
            if (sex == 1):
                male += 1
            elif sex == 2:
                female += 1
            else:
                other += 1
        # 计算总数再算比例
        total = len(friends[1:])
        #控制台输出
        # 打印下男女好友比例
        #print(u"男性好友:%.2f%%" % (float(male) / total * 100))
        #print(u"女性好友:%.2f%%" % (float(female) / total * 100))
        #print(u"其他:%.2f%%" % (float(other) / total * 100))
        #柱状图输出
        #bar=Bar(u'%s的微信好友性别比例' % (friends[0]['NickName']), 'from WeChat')
        #bar.add("性别",["男性","女性","其他"],[(float(male) / total * 100),(float(female) / total * 100),(float(other) / total * 100)])
        #bar.show_config()
        #bar.render(r"d:\pic\my_first_chart.html")
        list_sex=["男性","女性","其他"]
        list_value=[(float(male) / total * 100),(float(female) / total * 100),(float(other) / total * 100)]
        pie=Pie(u'%s的微信好友性别比例' % (friends[0]['NickName']), 'from WeChat')
        pie.add("性别",list_sex,list_value,center=[45,50],is_random=True,radius=[30,75],rosetype='radius')
        pie.render(r"d:\pic\my_friends_sex.html")

    def __del__(self):
        #登出
        itchat.logout()


if __name__ == '__main__':
    me=mywechat()
    me.get_friends_sex()
    #me.get_friends_Signature()
    me.get_friends_city()
    #必须要手动登出才行
    me.__del__()

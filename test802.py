# -*- coding: utf-8 -*-
from selenium import webdriver

import unittest, time, re
import requests

#测试时候是一个用例一个用来来测试的 测试完一个才会开始下一个用例测试

class testLog(unittest.TestCase):

    def setUp(self):
        #每个用例初始化
        self.driver=webdriver.Chrome("D:\\eclipse\\chromedriver_win32\\chromedriver.exe")
        self.driver.implicitly_wait(30)#隐性等待 最长等30秒
        self.base_url="http://www.smefdd.com/"
        self.verificationErrors=[]#脚本运行时 错误的信息将被打印到这个列表中
        self.accept_next_alert=True #是否接受下一个警告

    def test_fqcloud_login2(self):
        driver = self.driver
        driver.get(self.base_url + "account/account/manage/login.html")
        driver.find_element_by_xpath('//*[@id="login_form"]/section/div/div[4]/div[2]/a').click()
    def test_fqcloud_login(self):
        #什么都不输入 点击提交 -username -pwd -captcha出现必填提示信息
        #能够正常登录
        #正确输入用户名和验证码 键盘输入密码656 提示密码长度在‘6~18之间’
        #正确输入用户名和验证码 键盘输入密码656656 提示用户名或密码错误
        #记住用户名功能 -没有
        #登录失败后 不能记录密码的功能 -登录失败后密码仍旧保存着
        #用户名和密码前后有空格的处理 - 用户名填写15 736 262 8 58 -提示用户名或密码错误
        #密码加密显示 - 已有-
        #验证码显示- -易于辨认 文字显示正常 刷新点击按钮正常
        #登录界面中的注册· 忘记密码 登出用的另一帐号登录是否正常
        #输入密码时 大写键盘开启的时候要有提示信息 - 该页面没有提示信息-
        driver=self.driver
        driver.get(self.base_url+"account/account/manage/login.html")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("15 736 262 8 58")
        driver.find_element_by_id("pwd").clear()
        driver.find_element_by_id("pwd").send_keys("123456")
        # #验证码点击功能
        # for n in range(20):
        #     time.sleep(1)
        #     driver.find_element_by_id('imgCode').click()
        #     #点击后等待一秒查看验证码
        #忘记密码 链接是否正确 -该链接正常 -   
        #driver.find_element_by_xpath('//*[@id="login_form"]/section/div/div[4]/div[1]/a').click()
        #立即注册按钮是否正常 - 该链接正常
        #driver.find_element_by_xpath('//*[@id="login_form"]/section/div/div[4]/div[2]/a').click()

        #driver.find_element_by_name("captcha").clear()
        #driver.find_element_by_name("captcha").send_keys("8888")

        #driver.find_element_by_xpath("//button[@type='button']").click()
    def tearDown(self):
        time.sleep(10)#每个用例尝试完毕后等10秒
        self.driver.quit()#用例结束后退出浏览器

if __name__=='__main__':
    unittest.main()
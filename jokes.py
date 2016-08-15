# -*- coding: utf-8 -*-
import requests
from random import randint
from lxml import etree

url='http://www.qiushibaike.com/text/'
r = requests.get(url)
tree = etree.HTML(r.text)
contentlist = tree.xpath('//div[contains(@id, "qiushi_tag_")]')
jokes = []

for i in contentlist:
    content = i.xpath('div[@class="content"]/text()')
    contentstring = ''.join(content)
    contentstring = contentstring.strip('\n')
    jokes.append(contentstring)
print jokes[randint(0,len(jokes))]

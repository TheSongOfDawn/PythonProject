# -*- coding: UTF-8 -*-
from monitor import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    print("******Watching:******\n")
    monitorMain() #统计
    print("******monitorMain() over!!******")
    from analysis import *
    ResourceAnalysis() #分析
    print("******ResourceAnalysis() over!!******")
    #from drawLog import *
    #perfstatMain() #绘图
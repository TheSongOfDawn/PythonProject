# -*- coding: UTF-8 -*-

import ConfigParser



def readConfig():
    cf=ConfigParser.ConfigParser() #实例化一个对象
    config_dir="config/monitor.ini"

    cf.read(config_dir)
    secs=cf.sections()  #返回list

    #获取要监视的进程
    processes=cf.options("processName")
    process_list=[]
    for process in processes:
        #print cf.get("processName",process).decode(encoding="utf-8")
        process_list.append(cf.get("processName",process).decode(encoding="utf-8"))
    #获取监视时间
    overSeeTime=cf.getint("overSeeTime","time")

    watchList=[]
    #获取是否开启各项监视
    watchCPU=cf.getint("cpu","keepWatch")
    watchList.append(watchCPU)
    watchMem=cf.getint("mem","keepWatch")
    watchList.append(watchMem)
    watchIo=cf.getint("io","keepWatch")
    watchList.append(watchIo)
    watchNet=cf.getint("net","keepWatch")
    watchList.append(watchNet)

    return process_list,overSeeTime,watchList

'''
读取config/monitor.ini
'''
__author__ = 'osero'

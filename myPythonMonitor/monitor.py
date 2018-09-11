# -*- coding: UTF-8 -*-

import os
import sys
import psutil
import time
import datetime
import platform
from readConfig import *


class monitor(object):
    def __init__(self,pid_list,monitor_time,watchList):
        self.pid_list = pid_list
        self.monitor_time = monitor_time
        self.perflog = "./perflog/"
        self.perfimg = "./perfimg/"
        self.watchcpu=watchList[0]
        self.watchmem=watchList[1]
        self.watchio=watchList[2]
        self.watchnet=watchList[3]
    def dirRequired(self):
        if not os.path.exists(self.perflog) :
            os.makedirs(self.perflog)
        if not os.path.exists(self.perfimg):
            os.makedirs(self.perfimg)

    def monitorRunner(self):
        self.dirRequired()
        try:
            monitorsecond = self.monitor_time * 60
            begintime = (int)(time.time())
            p_list = []
            for pid in self.pid_list:
                p_list.append(psutil.Process(int(pid)))
            while(((int)(time.time()) - begintime) <= monitorsecond):
                for p in p_list:
                    name = p.name()
                    current = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    if self.watchmem :
                        memusage = p.memory_info().rss/1024.0/1024.0  # 返回的是B 这里处理成MB
                        memusagestr = current + "\t" + str(memusage) + "\n"
                        memusagestr_filepath = self.perflog + "mem" + "-" + name + "-" + str(p.pid) + ".log"
                        fp=open(memusagestr_filepath,"a")
                        fp.write(memusagestr)
                        fp.close()
                    if self.watchcpu :
                        cpuusage = p.cpu_percent()
                        cpuusagestr = current + "\t" + str(cpuusage) + "\n"
                        cpuusagestr_filepath = self.perflog + "cpu" + "-" + name + "-" + str(p.pid) + ".log"
                        fp=open(cpuusagestr_filepath,"a")
                        fp.write(cpuusagestr)
                        fp.close()
                    if self.watchio:
                        iousage = p.io_counters()  #返回B 下方处理成KB
                        iousagestr = current + "\t" + str(iousage[2]/1024.0) + "\t" + str(iousage[3]/1024.0) +"\n"
                        iousagestr_filepath = self.perflog + "io" + "-" + name + "-" + str(p.pid) + ".log"
                        fp=open(iousagestr_filepath,"a")
                        fp.write(iousagestr)
                        fp.close()
                    if self.watchnet:
                        pass
                time.sleep(1)

        except Exception as e:
            print(e)
        finally:
            pass


def findPidsToMonitor(processes):
    #获取当前操作系统
    sysstr = platform.system()
    pids_list=[]
    if(sysstr =="Windows"):
        #print ("Call Windows tasks")
        pids_list=windowsTask(processes)
    elif(sysstr == "Linux"):
        #print ("Call Linux tasks")
        pids_list=linuxTask(processes)
    else:
        pass
    return pids_list

def linuxTask(processes):
    cmdToRun="ps aux"
    result=os.popen(cmdToRun)
    strResult=result.read() #<type 'str'>
    listResult=strResult.split('\n') #<type 'list'>
    listNum=[]
    for oneResult in listResult:  # 对于每一项结果
        for process in processes:  # 对于每一个要监视的对象
            if oneResult.find(process) != -1:
                #print(oneResult)
                a=re.split(r'[\s]',oneResult)  #按所有空白字符来切割：\s
                for x in a:
                    if x.isdigit():
                        #print(x)  #pid
                        listNum.append(x)
                        break
    return listNum

def windowsTask(processes):
    pids_list=[]
    for process in processes:
        pid=get_proc_by_name(process)
        if pid != None:
            pids_list.append(pid)
    return pids_list

'''
windows 下方法
'''
def get_proc_by_name(pname):
    """ get process by name
    return the first process if there are more than one
    """
    for proc in psutil.process_iter():
        try:
            if proc.name().lower() == pname.lower():
                return proc.pid  # return if found one
        except psutil.AccessDenied:
            pass
        except psutil.NoSuchProcess:
            pass
    return None

if __name__=='__main__':
    config_list=readConfig()
    pid_list = findPidsToMonitor(config_list[0])
    print(pid_list)
    monitor_time =config_list[1]
    perfm = monitor(pid_list, monitor_time,config_list[2])
    perfm.monitorRunner()

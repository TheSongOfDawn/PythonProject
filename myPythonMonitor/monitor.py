# -*- coding: UTF-8 -*-

import os
import re
import sys
import time
import datetime
import platform
from readConfig import *
from psutil import *


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
                p_list.append(Process(int(pid)))
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
                    key_info, old_recv, old_sent = get_key()
                time.sleep(1)
                #  net
                if self.watchnet:
                    current = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    key_info, now_recv, now_sent = get_key()
                    net_in = {}
                    net_out = {}
                    for key in key_info:
                        net_in.setdefault(key, (now_recv.get(key) - old_recv.get(key)) / 1024)  # 每秒接收速率
                        net_out.setdefault(key, (now_sent.get(key) - old_sent.get(key)) / 1024) # 每秒发送速率
                    
                    netusagestr_filepath = self.perflog + "net.log"
                    fp=open(netusagestr_filepath,"a")
                    for key in key_info:
                        fp.write('%s\t%s\nInput:\t %-5sKB/s\nOutput:\t %-5sKB/s\n' % (current,key, net_in.get(key),\
                        net_out.get(key)))
                    fp.close()
        except Exception as e:
            print(e)
        finally:
            pass


def get_key():
 
    key_info = net_io_counters(pernic=True).keys()  # 获取网卡名称
 
    recv = {}
    sent = {}
 
    for key in key_info:
        recv.setdefault(key, net_io_counters(pernic=True).get(key).bytes_recv)  # 各网卡接收的字节数
        sent.setdefault(key, net_io_counters(pernic=True).get(key).bytes_sent)  # 各网卡发送的字节数
    return key_info, recv, sent


           
def monitorMain():
    # ******** 读取配置文件********
    config_list=readConfig()
    # ******** 获取要监视的文件的PID **********
    pid_list = findPidsToMonitor(config_list[0])
    print(pid_list)
    #********** 监视时间************
    monitor_time =config_list[1]
    #********* 生成监视器 ************
    perfm = monitor(pid_list, monitor_time,config_list[2])
    # **************开始监视 *********
    perfm.monitorRunner()

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
    for proc in process_iter():
        try:
            if proc.name().lower() == pname.lower():
                return proc.pid  # return if found one
        except AccessDenied:
            pass
        except NoSuchProcess:
            pass
    return None

if __name__=='__main__':
    config_list=readConfig()
    pid_list = findPidsToMonitor(config_list[0])
    print(pid_list)
    monitor_time =config_list[1]
    perfm = monitor(pid_list, monitor_time,config_list[2])
    perfm.monitorRunner()

'''
参考
gitHub:
https://github.com/junneyang/perfmonitor
psutil官方文档
https://psutil.readthedocs.io/en/latest

程序每次开始压缩前都会清除perflog目录

关于IO这里只看读写(累计)字节 在第 2 3 位
pio(read_count=, write_count=, read_bytes=, write_bytes=, read_chars=, write_chars=)

cpu_percent 返回一个浮点数，表示进程CPU利用率百分比.
注意 如果进程在不同的CPU内核上运行多个线程，则返回值可以> 100.0。

运行完毕后会压缩文件到当前目录下 然后会剪切到/home/like/perfmonitor/tardir
'''

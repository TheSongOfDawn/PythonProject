# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy
import math
import pytz
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
import datetime
import time
import sys
import os



def get_mem_stat_data(filepath):
    fp=open(filepath)
    mem_stat_data=[]
    for line in fp:
        line=line.strip()
        line_list=line.split("\t")
        mem_stat_data.append(line_list)
    fp.close()
    return mem_stat_data

def get_query_period_distribution_plot(stat_type, mem_stat_data, savefile):
    fig = plt.figure(figsize=(10,10))  # 设置画布大小
    ax = fig.add_subplot(111)  #将画布分成1行 1列 图像画在从左到右从上到下的第1块
    xaxis = ax.xaxis
    yaxis = ax.yaxis
    yList=[]
    dateList=[]
    if stat_type=='cpu' or stat_type=='mem':
        for item in mem_stat_data:
            dateList.append(item[0])
            try:
                assert(type(eval(item[1])) == float or type(eval(item[1])) == int)
                yList.append(float(item[1])) #转化成数字才会正常显示 y轴
            except:
                yList.append(0)
        dates=[datetime.datetime.strptime(item, "%Y-%m-%d %H:%M:%S") for item in dateList]
        ax.plot_date(dates,  yList,  '-',  marker='None',  linewidth=1)

    elif stat_type=='io':
        yList2=[]
        for item in mem_stat_data:
            dateList.append(item[0])
            try:
                assert(type(eval(item[1])) == float or type(eval(item[1])) == int)  #取出IO
                yList.append(float(item[1])) #同上
                yList2.append(float(item[2]))
            except:
                yList.append(0)

        dates=[datetime.datetime.strptime(item, "%Y-%m-%d %H:%M:%S") for item in dateList]
        ax.plot_date(dates,  yList,  '-',  marker='None',  label='Read',linewidth=1)
        ax.plot_date(dates,  yList2,  '-',  marker='None', label='Write', linewidth=1)
    ax.xaxis.set_major_formatter( DateFormatter('%Y-%m-%d %H:%M:%S') )
    ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')

    name=savefile.split("/")[2].split(".")[0]
    plt.title(name)
    plt.xlabel(u'Time')
    if(stat_type == "mem"):
        plt.ylabel(u'memUsage-MB')
    elif(stat_type == "cpu"):
        plt.ylabel(u'cpuUsage-%')
    elif(stat_type == "io"):
        plt.ylabel(u'IOUsage-KB')
    plt.grid(True)
    fig.autofmt_xdate()
    plt.savefig(savefile)
    plt.close('all')  # 解决内存爆表问题

def perfstatMain():
    file_dir = "../perflog/"
    img_file_dir = "../perfimg/"
    file_list = os.listdir(file_dir)
    #print file_list
    for item in file_list:
        if(item.split("-")[0] == "cpu"):
            stat_type = "cpu"
        elif(item.split("-")[0] == "mem"):
            stat_type = "mem"
        elif(item.split("-")[0] == "io"):
            stat_type = "io"
        print("file_dir+item:%s"%(file_dir+item))
        if(os.path.isfile(file_dir+item)):
            mem_stat_data=get_mem_stat_data(file_dir+item)
            get_query_period_distribution_plot(stat_type, mem_stat_data, img_file_dir + item + ".perf_stat_plot.png")

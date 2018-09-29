# -*- coding: UTF-8 -*-

import sys
import datetime
import time
import os

'''
对资源进行分析
求出每个文件的最大值 最小值 平均值
    处理cpu mem io
'''
def analysis(stat_type,filepath):
    print(stat_type)
    print(filepath)
    __console__=sys.stdout
    fp=open(filepath)
    fp2=open("ResourceAnalysis.txt","a")
    sys.stdout=fp2
    begin_time=''
    begin_flag=True
    end_time=''
    max_time=''  #最大值的时间 最小值的时间 
    min_time=''
    
    max=0  #最大值
    min=1024
    avg=0
    
    count=0  #计数器
    all=0    #所有的值
    lines=fp.readlines()
    if stat_type == "mem" or stat_type == "cpu": 
        if stat_type == "mem":
            unit="MB"
        else:
            unit="%"
        for line in lines :
            line_list=line.split('\t')
            if begin_flag:  #获取最开始的时间
                begin_time=line_list[0]
                begin_flag=False
            count=count+1  
            end_time=line_list[0]
            
            temp=float(line_list[1])
            all=all+temp
            if min>temp:  #value and time
                min_time=line_list[0]
                min=temp
            if max< temp:
                max_time=line_list[0]
                max=temp
        print("filepath:%s"%filepath) #文件名
        print("begin_time :%s"%begin_time)
        print("end_time :%s"%end_time)
        print("Max Usage:%.4f%s Time of occurrence：%s"%(max,unit,max_time))
        print("Min Usage:%.4f%s Time of occurrence：%s"%(min,unit,min_time))
        print("All is:%.4f counted is %.4f Avg is %.4f"%(all,count,all/count))
        
    elif stat_type == "io" : #io的单位为kb
        unit="kb"
        max_read=0
        max_write=0
        max_read_time=''
        max_write_time=''
        
        min_read=1024
        min_write=1024
        min_read_time=''
        min_write_time=''
        
        all_read=0
        all_write=0
        for line in lines :
            line_list=line.split('\t')
            if begin_flag:  #获取最开始的时间
                begin_time=line_list[0]
                begin_flag=False
                base_read=float(line_list[1])
                base_write=float(line_list[2])
                continue
            count=count+1  
            end_time=line_list[0]
            
            temp_read=float(line_list[1])-base_read # read write 是累计的 所以这里获取这一秒的增量 看哪一个时候最多
            temp_write=float(line_list[2])-base_write 
            
            all_read=all_read+temp_read
            all_write=all_write+temp_write
            
            base_read=float(line_list[1])  #重新给基准赋值
            base_write=float(line_list[2])

            if max_read < temp_read:  #最大读写
                max_read=temp_read
                max_read_time=line_list[0]
            if max_write < temp_write:
                max_write=temp_write
                max_write_time=line_list[0]
                
            if min_read >temp_read:  #最小读写
                min_read=temp_read
                min_read_time=line_list[0]
            if min_write >temp_write:  #最小读写
                min_write=temp_write
                min_write_time=line_list[0]
        
        print("filepath:%s"%filepath) #文件名
        print("begin_time :%s"%begin_time)
        print("end_time :%s"%end_time)
        print("Max Read:%.4f%s Time of occurrence：%s"%(max_read,unit,max_read_time))
        print("Max Write:%.4f%s Time of occurrence：%s"%(max_write,unit,max_write_time))
        print("Min Read:%.4f%s Time of occurrence：%s"%(min_read,unit,min_read_time))
        print("Min Write:%.4f%s Time of occurrence：%s"%(min_write,unit,min_write_time))
        
        print("All is:%.4f\t%.4f counted is %.4f Avg is %.4f\t%.4f"%(all_read,all_write,count,all_read/count,all_write/count))
    print("\n\n")
    fp.close()
    fp2.close()
    sys.stdout=__console__
def ResourceAnalysis():
    file_dir = "perflog/"  
    file_list = os.listdir(file_dir)
    for item in file_list:
        if(item.split("-")[0] == "cpu"):
            stat_type = "cpu"
        elif(item.split("-")[0] == "mem"):
            stat_type = "mem"
        elif(item.split("-")[0] == "io"):
            stat_type = "io"
        # 获取所属
        if(os.path.isfile(file_dir+item)):
            analysis(stat_type,file_dir+item)
        
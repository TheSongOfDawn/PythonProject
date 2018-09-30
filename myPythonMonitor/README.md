# 简单的Python监视进程脚本

## 使用方法:
    在config/monitor.ini 中写入要监视程序的名称,时间,项目.
    在主目录启动main开始监视，监视情况写入到perlog文件夹中。
    监视时间结束后，分析进程的cpu,io,mem的峰值，最低值，平均值.结果写入到ResourceAnalysis.txt中.

# 遇到过的问题

    ## Linux下: cannot import name _psutil_linux
        解决思路:
             from . import _psutil_linux as cext 这一行要找的是_psutil_linux.so文件，但上传的文件中没有
             用gcc生成一下.so文件，放到psutil中就行了

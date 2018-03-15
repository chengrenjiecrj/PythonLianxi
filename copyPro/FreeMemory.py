#!/usr/bin/env python
# -*- coding:utf8 -*-
# @Time     : 2017/11/30 14:25
# @Author   : hantong
# @File     : count_free_memory.py
#统计linux系统空闲内存和所有内存
with open('/proc/meminfo') as fd:
    for line in fd:
        if line.startswith('MemTotal'):
#startswith是以。。。开头的字符串，上面表示以MemTotal开头的字符串
            total = line.split()[1]
#split切片，上面表示下标1的字符串
            continue
        if line.startswith('MemFree'):
            free = line.split()[1]
            break
TotalMem = int(total)/1024000.0
#此处除以1024000，换算下来是GB
FreeMem = int(free)/1024000.0
print('Free Memory = '+"%.2f" % FreeMem +'G')
#%.2f表示保留两位小数
print('Total Memory = '+"%.2f" % TotalMem +'G')
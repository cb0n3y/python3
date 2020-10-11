#!/usr/bin/python
# _*'_ coding: utf-8 _*_'


from __future__ import print_function
import psutil


partitions = psutil.disk_partitions()


for part in partitions:
    if part.mountpoint == '/':
        if 'ro' in part.opts:
            print(0)
        else:
            print(1)
 

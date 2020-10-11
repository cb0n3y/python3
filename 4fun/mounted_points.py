#!/usr/bin/env python
# _*_ coding: utf-8 _*_


"""
    Author: cb0n3y
    Version: 1.0
    How to use: mounted_points.py path
    Description:l
"""

import os
import sys


def check_mounted_points():
    if os.path.ismount(sys.argv[1]):
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    check_mounted_points()

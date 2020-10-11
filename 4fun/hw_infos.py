#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


import os
import subprocess


def get_hw_information():
    print("[+] Gathering Hardware Information...\n")
    _cpus = os.cpu_count()
    print(_cpus)


if __name__ == '__name__':
    get_hw_information()

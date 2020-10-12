#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


import os
import sys


def get_cpu_number() -> object:
    _cpus_total = os.cpu_count()
    _cpus_physical = (int(_cpus_total // 2))
    _cpus_threads = _cpus_physical
    print("[+] Gathering Hardware Information...\n")
    print(f"[+] Target has:\n\t{int(_cpus_physical)} Cores\n\t{int(_cpus_threads)} Threads.")


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            print(f"[-] You need an argument\npython{sys.version[:3]} {sys.argv[0]} <OBJECT>"
                  f"\ne.g.: python{sys.version[:3]} {sys.argv[0]} cpu")
            print("[*] Possible values are: [cpu,memory,interface].")
            exit(1)
        else:
            """
               I check if the user input is equal cpu or not. It does not 
               matter if the user enter 'CPU' or 'cpu', the script will 
               always make lower cases out of it (sys.argv[1].lower()).
            """
            if sys.argv[1].lower() == 'cpu':
                get_cpu_number()
            elif sys.argv[1].lower() == 'memory':
                print("hello")
            elif sys.argv[1].lower() == 'interface':
                print("hello")
    except IndexError as index0:
        print(f"[-] Error: {index0}")
    except OSError as err:
        print(f"[-] Error: {err}")
    except IOError as io:
        print(f"[-] Error: {io}")

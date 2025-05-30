# coding=utf-8

#!/usr/bin/env python3


import sys

def check_modules():
    try:
        import colorama
    except Exception as e:
        print("[-] 'colorama' package not installed!")
        print("[*] Type 'pip install colorama' to install!")
        print(e)
        sys.exit(0)

    try:
        import asyncio
    except:
        print("[-] 'asyncio' package not installed!")
        print("[*] Type 'pip install asyncio' to install!")
        sys.exit(0)
    try:
        import warnings
    except:
        print("[-] 'warnings' package not installed!")
        print("[*] Type 'pip install warnings' to install!")
        sys.exit(0)

    import warnings
    warnings.filterwarnings("ignore")

    from colorama import init
    init()
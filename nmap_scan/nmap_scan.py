#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import subprocess  

def nmap_scan(target):
    try:
        result = subprocess.check_output(['nmap',  '-T4', '-A', target])
        print(result.decode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")

def scan_target(target):
    print(f"Scanning {target}...")
    nmap_scan(target)

if __name__ == "__main__":
    targets = input("ip: ").split()
    
    threads = []
    for target in targets:
        thread = threading.Thread(target=scan_target, args=(target,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("扫描完成")

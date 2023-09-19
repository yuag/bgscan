#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import requests
import subprocess
import csv
import sys
import urllib3
import tkinter as tk

from nmap_scan.nmap_scan import nmap_scan
from awvs.awvs import AwvsScanGUI
from pocsuite3.pocsuite3 import run_pocsuite_scan
from fofa.fofa import search_domain
from tkinter import ttk
from nuclei.nuclei import NucleiScan
from socks5.sk5 import proxy

from xray.xray    import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
from xray.xray    import MyMainWindow


# 禁用urllib3警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



# 定义你的钉钉机器人Webhook地址
dingding_webhook_url = "https://oapi.dingtalk.com/robot/send?access_token=秘钥"

# 发送消息到钉钉机器人
def send_dingding_message(message):
    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "text",
        "text": {
            "content": message
        }
    }
    response = requests.post(dingding_webhook_url, json=data, headers=headers)

    if response.status_code == 200:
        print("\033[35m消息已成功发送到钉钉机器人\033[0m")
    else:
        print(f"消息发送失败，错误码：{response.status_code}")





def main():
    VERSION_STRING = """\033[0;32m
                            bgscan漏洞集成工具  V1.0
                            
                    githup：https://github.com/yuag/bgscan
    \033[0m"""

    print(VERSION_STRING)

    while True:
        print("\033[33m 1. Nmap \033[0m") 
        print("\033[34m 2. wvs  \033[0m")
        print("\033[32m 3. pocsuite3  \033[0m")
        print("\033[31m 4. fofa \033[0m") 
        print("\033[35m 5. nuclei  \033[0m")
        print("\033[33m 6. 代理下载 \033[0m")
        print("\033[36m 7. xray  \033[0m")
        print("\033[0m 10. 退出  \033[0m")
        choice = input("选择模块: ")


        if choice == '1':
            target = input("ip地址: ")
            nmap_scan(target)
            send_dingding_message(f"Nmap扫描完成  {target}")  
        elif choice == '2':
            awvs_app = AwvsScanGUI()
            awvs_app.mainloop()
            send_dingding_message("AWVS扫描完成")
        elif choice == '3':
            target = input("输入网站 : ")
            poc_file_path = input("本地poc路径 : ")
            run_pocsuite_scan(target, poc_file_path)
            send_dingding_message(f"Pocsuite3扫描完成  {target}")
        elif choice == '4':
            target = input("输入fofa搜索条件: ")
            search_domain(target)
            subprocess.run(['python3', 'fofa.py', '-u', target, '-o'])
            send_dingding_message(f"fofa扫描完成  {target}")
        elif choice == '5':
            root = tk.Tk()
            app = NucleiScan(root)
            root.mainloop()
            send_dingding_message("NucleiScan扫描完成")          
        elif choice == '6':
            socks5_api = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all"
            socks5 = "socks5.txt"
            http_api = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"   
            http = "http.txt"
            socks4_api = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all"
            socks4 = "socks4.txt"                
            proxy(socks5_api, socks5)
            proxy(http_api, http)
            proxy(socks4_api, socks4)  
            send_dingding_message(f"代理扫描完成")
        elif  choice == '7':
            app = QApplication(sys.argv)
            main_window = MyMainWindow()
            main_window.show()
            sys.exit(app.exec_())
            send_dingding_message("xray扫描完成")  
        elif choice == '10':
            print("\033[36m退出扫描，Goodbye!\033[0m")
            break
        else:
            print("\033[35m输入无效模块,请重新输入\033[0m")

if __name__ == "__main__":
    main()

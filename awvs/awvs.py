#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import tkinter as tk
import json
import requests
from tkinter import filedialog
import urllib3
import subprocess

urllib3.disable_warnings()

class AwvsScanGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Awvs Scan GUI")
        self.geometry("400x200")

        self.scanner_entry = tk.Entry(self)
        self.scanner_entry.pack()
        self.scanner_entry.insert(tk.END, "wvs地址")  

        self.api_entry = tk.Entry(self)
        self.api_entry.pack()
        self.api_entry.insert(tk.END, "秘钥")  

        self.browse_button = tk.Button(self, text="添加URL", command=self.browse_file)
        self.browse_button.pack()

        self.start_button = tk.Button(self, text="开始", command=self.start_scan)
        self.start_button.pack()

        self.result_label = tk.Label(self)
        self.result_label.pack()

        self.file_path = ""

    def browse_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

    def start_scan(self):
        scanner_url = self.scanner_entry.get()
        api_key = self.api_entry.get()

        headers = {'X-Auth': api_key, 'content-type': 'application/json'}

        def scan_target(website):
            try:
                data = {
                    'address': website,
                    'description': 'awvs-auto',
                    'criticality': '10'
                }
                response = requests.post(f'{scanner_url}/api/v1/targets', data=json.dumps(data), headers=headers, verify=False)
                if response.status_code == 201:
                    print(f'Successfully added target: {website}')
                else:
                    print(f'Failed to add target: {website}')
            except Exception as e:
                print(f'Error: {str(e)}')

        if self.file_path:
            try:
                success_count = 0
                failure_count = 0

                with open(self.file_path) as file:
                    websites = [line.strip('\n\r') for line in file]

                threads = []
                for website in websites:
                    thread = threading.Thread(target=scan_target, args=(website,))
                    threads.append(thread)
                    thread.start()

                for thread in threads:
                    thread.join()
                    success_count += 1

                result_message = f"添加成功的URL数量: {success_count}\n添加失败的URL数量: {failure_count}"
                self.result_label.config(text=result_message)


                command = "123"  # 
                output = subprocess.check_output(command, shell=True, text=True)
                print("Command Output:")
                print(output)

            except Exception as e:
                print(f'Error: {str(e)}')
        else:
            print("请先选择一个文件")

if __name__ == "__main__":
    app = AwvsScanGUI()
    app.mainloop()

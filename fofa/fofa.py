import base64
import argparse
import time
import requests
import sys
import io
import csv
import argparse
import os
import threading
from concurrent.futures import ThreadPoolExecutor

email = ""
key = ""
search_size = "10"  # 扫描数多少条
name = "fofa"

# 删除重复URL
processed_urls = set()

def search_domain(domain):
    if domain in processed_urls:
        print(f"URL {domain} 已处理，跳过")
        return

    processed_urls.add(domain)  # 将URL添加到已处理集合中

    url = "https://fofa.info/api/v1/search/all/"
    params = {
        'email': email,
        'key': key,
        'qbase64': base64.b64encode(f'domain="{domain}"'.encode()).decode(),
        'size': search_size,
        'fields': 'ip,port,host,title,server'
    }
    r = requests.get(url, params=params)
    res = r.json()
    print(res)

    if 'error' in res and res['error']:
        errmsg = res.get('errmsg', 'Unknown error')
        print(f"FOFA API error: {errmsg}")
        return

    size = res.get('size', 0)
    print(f"Total results: {size}")

    if size > 0:
        result = res.get('results', [])

        with open(f'{name}_{domain}.csv', 'w', newline='', encoding="gb18030") as f:
            f_csv = csv.writer(f)
            f_csv.writerow(["IP:Port", "Host", "Title", "Server"])
            for r in result:
                f_csv.writerow([f'{r[0]}:{r[1]}', r[2], r[3], r[4]])

def parser():  # 创建命令行参数
    parser = argparse.ArgumentParser(description='获取URL信息')
    parser.add_argument('-u', '--url', default=None, type=str, help='获取单个域名信息')
    args = parser.parse_args()
    return args

def multi_threading(urls):
    with ThreadPoolExecutor(max_workers=100) as executor:
        for url in urls:
            executor.submit(search_domain, domain=url)

args = parser()  # 从command 获取的参数
if args.url:
    urls = [args.url]
    multi_threading(urls)

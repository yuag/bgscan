# bgscan
bgscan漏洞集成工具

<br>
<br>


# 1.项目文件结构：

```
├── bgscan.py
├── awvs
│   ├── awvs.py
│   └── url.txt
├── bgscan.py
├── fofa
│   ├── __init__.py
│   └── fofa.py
├── nmap_scan
│   ├── __init__.py
│   └── nmap_scan.py
├── nuclei
│   ├── nuclei.py
│   ├── poc
│   │   ├── xss-fuzz.yaml
│   │   ├── xss-path.yaml
│   │   ├── xss-reflected.yaml
│   │   ├── xss-stored.yaml
│   │   ├── xxe.yaml
│   │   ├── xxe_lfi.yaml
│   │   ├── xxljob-panel.yaml
│   │   ├── xxljob-workflow.yaml
│   │   └── yapi-workflow.yaml
│   └── url.txt
├── pocsuite3
│   ├── __init__.py
│   ├── poc
│   │   ├── ActiveMQ_put_CVE_2016_3088.py
│   │   ├── Apache 2.4.49 Path Traversal.py
│   │   ├── activemq_cve-2015-1830_unauthorized_rce.py
│   │   └── admin_login_Bypass.py
│   └── pocsuite3.py
├── socks5
│   ├── sk5.py
│   └── socks5.txt
└── xray
    ├── __init__.py
    ├── config.yaml
    ├── module.xray.yaml
    ├── plugin.xray.yaml
    ├── url.txt
    ├── xray.py
    ├── xray.yaml
    └── xray_darwin_amd64
```

<br>
<br>

# 2.功能说明

| 编 号          | 选项           | 说明           |  安装|
|  -------------| ------------- | ------------- |------------- |
| 1  | Nmap  | 命令  |   |
| 2  | wvs  |  GUI |    |   
| 3  | pocsuite3  | 命令 |   
| 4  | fofa    | 命令  |  
| 5  | nuclei  | GUI  | nuclei下载系统适应版本  |
| 6  | 代理下载  | 命令 |   |
| 7  | xray  | GUI  |  |
| 10  | 退出  |   | 
<br>
<br>

# 3.环境配置

1、测试环境Mac，所有命令都是python3执行的。

2、Python版本：3.7以上版本(本机测试3.11)。

3、使用带(GUI)系统，不然有一些工具没法使用。

4、 win下面使用有字体问题未解决。

<br>
<br>


# 4.使用方法

1.




















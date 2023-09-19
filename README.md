# bgscan
bgscan漏洞集成工具

![image](https://github.com/yuag/bgscan/assets/34123873/654e3d2a-225c-4654-9d72-e66301fbe291)



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

0.钉钉设置  
bgscan.py 31行代码设置钉钉机器人扫描完成提醒。

![image](https://github.com/yuag/bgscan/assets/34123873/4a5a0afa-2b98-4924-8853-c23bcda90fc8)

![image](https://github.com/yuag/bgscan/assets/34123873/1192a203-5f13-48f6-a17f-612524717372)


<br>
<br>
1.Nmap

![image](https://github.com/yuag/bgscan/assets/34123873/44ed684b-24a4-4317-893a-2b907fe1a7f0)




<br>
<br>

2.wvs

只有添加网站功能。

![image](https://github.com/yuag/bgscan/assets/34123873/861a5dce-ef9a-4108-b14d-7cbc87c57a52)




<br>
<br>
3.pocsuite3


![image](https://github.com/yuag/bgscan/assets/34123873/80a43891-33c3-48f8-a9bb-2034789edd53)

![image](https://github.com/yuag/bgscan/assets/34123873/1c5c9f3a-d3a3-4fe5-bdee-5bdcbf4010bb)




<br>
<br>
4.fofa扫描

bgscan.py  90行代码设置python3需设置自己的python环境执行命令。
<img width="737" alt="image" src="https://github.com/yuag/bgscan/assets/34123873/7f81e3bc-cbb4-43fe-9aa8-98f20a03da7c">



路径：bgscan\fofa\fofa.py
85到88行添加fofa账号秘钥

<img width="558" alt="image" src="https://github.com/yuag/bgscan/assets/34123873/3233694b-d629-4111-9a19-743932418b92">



![image](https://github.com/yuag/bgscan/assets/34123873/6d4a04fe-513a-4b6a-9070-d18f8d499091)




添加了URL去重功能<br>
执行成功保存在根目录下fofa_xxx.com.csv
<br>
<br>
5.nuclei

![image](https://github.com/yuag/bgscan/assets/34123873/0d1b7215-8425-4122-a344-1276b2cc8b5f)


根目录下面会出现扫描过程：nuclei.txt

nuclei下载系统适应版本：https://github.com/projectdiscovery/nuclei/releases

poc推荐下载地址：https://github.com/ExpLangcn/NucleiTP

<br>
<br>
6.代理下载

![image](https://github.com/yuag/bgscan/assets/34123873/e241b83d-2d09-4a9c-8629-4cb7b7cbad9e)



保存文件在根目录下，socks5,txt,socks4.txt

<br>
<br>
7.xray

xray目录下面执行一次xray，然后GUI在执行一次生成yaml在根目录下不然没法使用。(调用/加载一直显示少yaml文件，无法解决！！！)


![image](https://github.com/yuag/bgscan/assets/34123873/57fe2cb9-e7f4-45e4-9acb-4b7b6bd46508)


扫描结束有漏洞根目录下面有个 xray.html 文件
<br>
<br>





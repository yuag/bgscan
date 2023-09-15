# bgscan
bgscan漏洞集成工具：

<br>
<br>


# 1.项目文件结构：

```
├── README.md ##使用说明
├── fofamap.py ##fofamap主程序
│   ├── linux ##linux版主程序
│   │   ├── nuclei_386
│   │   ├── nuclei_amd
│   │   ├── nuclei_arm
│   │   └── nuclei_armv6
│   ├── macos ##macos版主程序
│   │   ├── nuclei_amd
│   │   └── nuclei_arm
│   └── windows ##windows版主程序
│       ├── nuclei_386.exe
│       └── nuclei_amd.exe
├── nuclei.py ##nuclei api调用类
├── requirements.txt ##依赖包要求
```

<br>
<br>

# 2.功能说明

| 编 号          | 选项           | 说明           | 
|  -------------| ------------- | ------------- |
| 1  | Nmap  | 命令  |   
| 2  | wvs  |  GUI |       
| 3  | pocsuite3  | 命令 |   
| 4  | fofa    | 命令  |  
| 5  | nuclei  | GUI  |   
| 6  | 代理下载  | 命令 |   
| 7  | xray  | GUI  |  
| 10  | 退出  |   | 
<br>
<br>

# 3.环境配置

1、测试环境Mac，所有命令都是python3执行的。

2、Python版本：3.7以上版本(本机测试3.11)。

3、使用带(GUI)系统，不然有一些工具没法使用。

<br>
<br>


# 4.使用方法

1.



















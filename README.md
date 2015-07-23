# scanAutoToxlsx
Nmap scan results will automatically import xlsx


## requirements

安装执行依赖，请在终端输入如下命令

    sudo pip install -r requirements.txt


## 须知

- 需要Excel 2007 以上，支持写入xlsx文件

- 因nmap扫描操作系统需要管理员权限，故在执行之前，请确定你的操作权限


## 用法

本脚本是读取网段内存活主机列表，然后对这些存活主机列表进行扫描

获取存活主机列表的命令，你可以参照如下：

    sudo nmap -sP -f -n --min-hostgroup 1024 --min-parallelism 1024 -oN 172.29.24.0_24 172.29.24.0/24

在获取存货主机扫描列表后，你可以用本脚本执行自动化扫描并写入xlsx文件。操作如下：

    sudo python scanOS.py 172.29.24.0_24 


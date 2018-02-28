#!/usr/bin/python
# -*- coding: UTF-8 -*-

import paramiko
import sys

# 配置
host="ninvfeng.com" #服务器
port=22 #端口
user="root" #用户名
key ="/Users/feng/.ssh/id_rsa" #可登陆服务器的私钥文件
path="/data/game/mc1.11.2" #我的世界游戏目录
file="minecraft_server.1.11.2.jar" #我的世界服务端主程序文件

# 连接服务器
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,user,key_filename=key)

# 启动|关闭
if (len(sys.argv)>1 and sys.argv[1]=='start'):
    ssh.exec_command('screen -r mc')
    stdin, stdout, stderr = ssh.exec_command('cd '+path+' && java -Xms1024M -Xmx1024M -jar '+file+' &')
    ssh.exec_command('screen -d')
elif (len(sys.argv)>1 and sys.argv[1]=='stop'):
    stdin, stdout, stderr = ssh.exec_command("kill `ps -ef | grep '"+file+"' | grep -v grep | awk '{print $2}'`")
else:
    print "start:启动  stop:关闭"
ssh.close()

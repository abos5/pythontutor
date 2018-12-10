#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys
import paramiko
import threading
def ssh2(ip,port,username,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,port,username,timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
#            stdin.write("Y") #简单交互，输入 ‘Y' ，用于执行命令需要有交互时用，不错需要按'ctrl'+'\'组合键才会退出生效，所以可以等待确定完成了工作。再退出。
            out = stdout.readlines()
            err = stderr.readlines()
#屏幕输出
            for o in out:
                print o,
            for i in err:
                print i,
        print '%sOK\n'%(ip)
        ssh.close()
    except Exception,ex:
        print Exception,":",ex
        print '%sError\n'%(ip)

if __name__=='__main__':
#    cmd = ['cal','sed -i \'s/find \/root -name \"\*\.log\"/xxxxx/g\' /var/spool/cron/root'] #你要执行的命令列表，一条命令用单引号括起来，多条命令之间用逗号隔开，执行的命令中带有如单引号，双引号，通配符等其他需要转义成普通字符的，那么需要加\转义符。
###下面这种方式是提前把执行的命令写入到文件中，一行一条。脚本去读取文件获取执行的命令
    cmds=open("/root/cmds.txt")
    cmd=cmds.readlines()
    cmds.close()
###下面是指定ssh的端口号，用户名
    port = "37671" #端口
    username = "root" #用户名
    threads = [] #多线程
    print "Begin......"
###ip循环遍历，有需求可以使用
#    for i in range(55,57):
#        ip = '10.66.59.'+str(i)
#        a=threading.Thread(target=ssh2,args=(ip,port,username,cmd))
#        a.start()
###ip从文件读取，一行一个，提前将需要批量操作的ip写入到文件中###
    hosts=open("/root/list.txt")
    host=hosts.readlines()
    hosts.close()
    for ip in host:
        a=threading.Thread(target=ssh2,args=(ip,port,username,cmd))
        a.start()

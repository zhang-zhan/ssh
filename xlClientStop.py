__author__ = 'zhangzhan'
#coding:utf-8
import pexpect

def ssh_cmd(ip, user, passwd, cmd):
    ssh = pexpect.spawn('ssh %s@%s "%s"' % (user, ip, cmd))
    r = ''
    try:
        i = ssh.expect(['password: ', 'continue connecting (yes/no)?'])
        if i == 0 :
            ssh.sendline(passwd)
        elif i == 1:
            ssh.sendline('yes')
    except pexpect.EOF:
        ssh.close()
    else:
        r = ssh.read()
        ssh.expect(pexpect.EOF)
        ssh.close()
    return r

#serverIp = '192.168.8.92'
#from hosts import serverIp
from hosts import slaveIp

user = 'root'
passwd = 'root'

#start server
# scmd = 'cd /home/ubuntu/tyServer; nohup python /home/ubuntu/tyServer/tyServer.py >/dev/null 2>&1 &'
# print "-- %s run:%s --" % (serverIp, scmd)
# ssh_cmd(serverIp,user,passwd,scmd)

#start slaves
cmd = 'cd /root/sinaGetToken; nohup python /root/sinaGetToken/stop.py >/dev/null 2>&1 &'
for ip in slaveIp:
         print "-- %s run:%s --" % (ip, cmd)
         print ssh_cmd(ip, user, passwd, cmd)

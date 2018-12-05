# coding=utf-8
from blinker import Namespace
from datetime import datetime
from flask import request,g

# 初始化一个命名空间对象
loginspace = Namespace()

# 创建

loginsingal = loginspace.signal('login')


# 两种方法接收信号信息
# def login_log(sender,username):
#     # 一旦用户登陆，就记录用户名，登陆时间，ip地址
#     now = datetime.now()
#     ip = request.remote_addr
#     log_line = "{username} * {now} * {ip}".format(username=username,now=now,ip=ip)
#     with open('D:\login_log.txt','a') as fp:
#         fp.write(log_line+'\n')
def login_log(sender):
    # 一旦用户登陆，就记录用户名，登陆时间，ip地址
    now = datetime.now()
    ip = request.remote_addr
    log_line = "{username} * {now} * {ip}".format(username=g.username,now=now,ip=ip)
    with open('D:\login_log.txt','a') as fp:
        fp.write(log_line+'\n')
loginsingal.connect(login_log)
import smtplib,time
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr
#纯文本文件

def format_addr(s):
    name,addr = parseaddr(s)
    return  formataddr((Header(name,"utf-8").encode(),addr))

from_addr ="q95linyu@163.com"
password = "960876917L"
to_addr = "1633883839@qq.com"
smtp_server = "smtp.163.com"

msg =  MIMEText("python test","plain","utf-8")
msg["From"] = format_addr("一号爬虫<%s>"%from_addr)
msg["To"] = format_addr("管理员<%s>"%to_addr)
msg["Subject"] = Header("一号爬虫状态","utf-8").encode()

server = smtplib.SMTP(smtp_server,25)
server.login(from_addr,password)
print ("login success")
server.sendmail(from_addr,[to_addr],msg.as_string())

server.quit()
print (time.clock())
print(type(str(time.clock())))






















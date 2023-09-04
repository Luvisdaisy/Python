from smtplib import SMTP, SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

# 发送邮件


def main():
    sender = 'qi_7ran@163.com'
    password = 'EJAOAOHOSPGEUTPK'
    # smtper_port = 469
    smtp_server = 'smtp.163.com'
    receivers = ['1078462128@qq.com', '3251168454@qq.com']
    message = MIMEText('用python 发送邮件', 'plain', 'utf-8')
    message['From'] = Header('王大锤', 'utf-8')
    message['To'] = Header('tian', 'utf-8')
    message['Subject'] = Header('示例代码', 'utf-8')

    try:
        smtper = SMTP(smtp_server)
        smtper.login(sender, password)
        smtper.sendmail(sender, receivers, message.as_string())
        smtper.quit()
        print('Email sent successfully!')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()

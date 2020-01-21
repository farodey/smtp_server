import smtplib
import email.utils
from email.mime.text import MIMEText

# Тело письма
msg = MIMEText('Добро пожаловать на UXCrowd!\n\n'
               'Ваши логин и пароль для входа в личный кабинет:\n\n'
               'Логин: ebilemmov-6678@yopmail.com\n\n'
               'Пароль: 4XlzXi\n\n'
               'Изменить пароль можно в личном кабинете в разделе Профиль.\n\n'
               'На связи,\n\n'
               'Команда UXCrowd', 'plain', 'utf-8')

msg['To'] = email.utils.formataddr(('Recipient', 'recipient@example.com'))
msg['From'] = email.utils.formataddr(('Author', 'author@example.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP('127.0.0.1', 1021)
server.set_debuglevel(True)     # show communication with the server
try:
    server.sendmail('author@example.com', ['recipient@example.com'], msg.as_string())
finally:
    server.quit()

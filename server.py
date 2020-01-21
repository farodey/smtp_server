import asyncore
import base64
import re
import smtpd


class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):

        # Декодируем тело письма
        bodyBytes = bytes(re.search(r"Subject: .*\n\n([\s\S]*)", data)[1], "utf-8")
        body = base64.b64decode(bodyBytes).decode("utf-8")

        # Ищем логин/пароль
        login = re.search(r"Логин: (.*?@yopmail.com)", body).group(1)
        password = re.search(r"Пароль: (\w{6})", body).group(1)

        # Пишем логин/пароль в файл
        with open('db.txt', 'a') as file:
            file.write(login)
            file.write(':')
            file.write(password)
            file.write('\n')


# Запускаем сервер
server = CustomSMTPServer(('127.0.0.1', 1021), None, decode_data=True)
asyncore.loop()

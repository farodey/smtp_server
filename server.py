import smtpd
import asyncore, re, base64


class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):

        # Декодируем тело письма
        a = data.find('Subject')
        b = data.find('\n\n', a)
        body = data[b + 2: len(data)]
        body = base64.b64decode(body).decode()

        # Ищем логин/пароль
        login = re.search(r"Логин: (.*?@yopmail.com)", body).group(1)
        password = re.search(r"Пароль: (\w{6})", body).group(1)

        # Пишем логин/пароль в файл
        with open('db.txt', 'a') as file:
            file.write(str(login))
            file.write(':')
            file.write(str(password))
            file.write('\n')


# Запускаем сервер
server = CustomSMTPServer(('127.0.0.1', 1021), None, decode_data=True)
asyncore.loop()

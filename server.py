import smtpd
import asyncore, re, base64


class CustomSMTPServer(smtpd.SMTPServer):
    count = 0

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):

        login = re.search(r"Логин: (.*?@hostname.com)", data)
        password = re.search(r"Пароль: (\w{6})", data)

        # Декодирует русские символы из письма
        a = data.find('Subject')
        b = data.find('\n\n', a)
        body = data[b + 2: len(data)]
        print(base64.b64decode(body).decode())

        with open('db.txt', 'a') as file:
            file.write(" ".join([str(self.count)]))

        self.count += 1


# Запускаем сервер
server = CustomSMTPServer(('127.0.0.1', 1021), None, decode_data=True)
asyncore.loop()

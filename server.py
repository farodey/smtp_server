import smtpd
import asyncore
import sqlite3


class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):

        # Подключаемся к базе данных
        conn = sqlite3.connect('email.db')
        cursor = conn.cursor()

        # Тут парсим из полученного письма email и password
        #
        #

        # Вставляем данные в таблицу
        cursor.execute("""INSERT INTO email_db VALUES ('blabla@gmail.com', 'pas123'""")

        # Сохраняем изменения
        conn.commit()

        # with open('db.txt', 'w') as file:
        #     file.write('Receiving message from:' + str(peer) + '\n')
        #     file.write('Message addressed from:' + str(mailfrom) + '\n')
        #     file.write('Message addressed to  :' + str(rcpttos) + '\n')
        #     file.write('Message length        :' + str(len(data)) + '\n')
        #     file.write(data.decode() + '\n')
        #     return


# Создаем базу данных и таблицу в ней
conn = sqlite3.connect('email.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE email_db (email text, password text)')

# Запускаем сервер
server = CustomSMTPServer(('127.0.0.1', 1025), None)
asyncore.loop()

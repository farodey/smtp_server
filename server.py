import smtpd
import asyncore


class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        with open('db.txt', 'a') as file:
            file.write('Receiving message from:' + str(peer) + '\n')
            file.write('Message addressed from:' + str(mailfrom) + '\n')
            file.write('Message addressed to  :' + str(rcpttos) + '\n')
            file.write('Message length        :' + str(len(data)) + '\n')
            file.write(data.decode() + '\n')
            return


server = CustomSMTPServer(('127.0.0.1', 1025), None)
asyncore.loop()

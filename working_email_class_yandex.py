import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class WorkWithEmail():
    def __init__(self):
        self.yandex_smtp = "smtp.yandex.ru"
        self.yandex_imap = "imap.yandex.ru"
        self.login = input('Enter login: ')
        self.password = input('Enter password: ')
        self.recipients = []

    def __append_recipients(self):
        enter_recipient = input('Enter recipient\'s email \
(or \'end\', if no more): ')
        while enter_recipient != 'end':
            self.recipients.append(enter_recipient)
            enter_recipient = input('Enter recipient\'s email \
(or space, if no more): ')
        print(f'Количество адресов в рассылке: {len(self.recipients)}')
        return self.recipients

    def __create_message_to_send(self):
        self.subject = input('Enter subject: ')
        self.recipients = self.__append_recipients()
        self.message = input('Enter message: ')

    def __prepare_to_send(self):
        message_to_send = MIMEMultipart()
        message_to_send['From'] = self.login
        message_to_send['To'] = ', '.join(self.recipients)
        message_to_send['Subject'] = self.subject
        message_to_send.attach(MIMEText(self.message))
        return message_to_send
    
    def __send_to_server(self, message_to_send):
        connect_server = smtplib.SMTP_SSL(self.yandex_smtp, 465)
        connect_server.login(self.login, self.password)
        connect_server.sendmail(message_to_send['From'], \
                                message_to_send['To'] , \
                                message_to_send.as_string())
        connect_server.quit()

    def send_message(self):
        self.__create_message_to_send()
        message_to_send = self.__prepare_to_send()
        self.__send_to_server(message_to_send)

    def get_message(self, header=None):
        mail = imaplib.IMAP4_SSL(self.yandex_imap)
        mail.login(self.login, self.password)
        mail.select("INBOX")
        criterion = '(HEADER Subject "%s")' \
            % header if header else 'ALL'
        _, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        _, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        mail.logout()
        return email.message_from_bytes(data[0][1]).get_payload()     


if __name__ == '__main__':
    work_with_email = WorkWithEmail()
    work_with_email.send_message()
    print(work_with_email.get_message(header='hello'))

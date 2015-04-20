import smtplib
# view this link re email using gmail
# https://support.google.com/mail/answer/78754


class PostalService():
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def send_mail(self, from_address, to_address, message_text):
        server = smtplib.SMTP(self.host)
        server.set_debuglevel(1)
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(from_address, to_address, message_text)
        server.quit()


if __name__ == "__main__":
    ps = PostalService("smtp.gmail.com", "your_email", "your_password")

    ps.send_mail("kevinelong@gmail.com", "kevin@cleverclever.com", "Hi,\n This is a test message.")
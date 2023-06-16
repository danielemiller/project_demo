import smtplib
from email.mime.text import MIMEText

class DemoClass:
    def __init__(self, name):
        self.name = name
        self.greetings = []

    def greet(self, greeting):
        self.greetings.append(greeting)
        return f'{greeting}, {self.name}!'

    def show_greetings(self):
        for greeting in self.greetings:
            print(f'{greeting}, {self.name}!')

    def send_email(self, smtp_server, port, username, password, from_addr, to_addr, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = to_addr

        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        server.quit()

if __name__ == '__main__':
    demo = DemoClass('ChatGPT')
    demo.greet('Hello')
    demo.greet('Hi')
    demo.greet('Hey')
    demo.show_greetings()
    demo.send_email('smtp.example.com', 587, 'username', 'password', 'from@example.com', 'to@example.com', 'Hello', 'This is the body of the email.')

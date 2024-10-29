import smtplib
from email.message import EmailMessage

password = 'bbkmvoxkvuudfltc'
from_email = 'oleg@pinco.ru'
to_email = 'olegpod@gmail.com'
title_mes = 'Тестовое письмо из питона'

message = EmailMessage()
message.set_content('Привет от питона')
message['Subject'] = title_mes
message['From'] = from_email
message['To'] = to_email

server = None

try:
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.login(from_email, password)
    server.send_message(message)
    print(f'Письмо на {to_email} с темой "{title_mes}" отправлено')
except Exception as e:
    print(f'Ошибка: {e}')
finally:
    if server:
        server.quit()

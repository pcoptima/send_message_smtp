import smtplib
from email.message import EmailMessage
from tkinter import *
from tkinter import messagebox as mb

password = 'bbkmvoxkvuudfltc'
from_email = 'oleg@pinco.ru'
to_email = 'olegpod@gmail.com'


def send_message():
    password = pass_entry.get()
    from_email = from_email_entry.get()
    to_email = to_email_entry.get()
    title_mes = sub_entry.get()
    text_message = mess_entry.get(1.0, END)
    message = EmailMessage()
    message.set_content(text_message)
    message['Subject'] = title_mes
    message['From'] = from_email
    message['To'] = to_email

    server = None

    try:
        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        server.login(from_email, password)
        server.send_message(message)
        mb.showinfo('Отправка email', f'Письмо на {
                    to_email} с темой "{title_mes}" отправлено')
    except Exception as e:
        mb.showerror('Ошибка', f'Ошибка: {e}')
    finally:
        if server:
            server.quit()


window = Tk()
window.title('Отправка письма')
window.geometry('600x350')

text_from = Label(window, text='От кого:', font=('Arial', 14))
text_from.grid(row=0, column=0, pady=5)

from_email_entry = Entry(window, font=('Arial', 14), width=30)
from_email_entry.grid(row=0, column=1, pady=5)

Label(window, text='Кому:', font=('Arial', 14)).grid(row=1, column=0, pady=5)
to_email_entry = Entry(window, font=('Arial', 14), width=30)
to_email_entry.grid(row=1, column=1, pady=5)

text_pass = Label(window, text='Пароль:', font=('Arial', 14))
text_pass.grid(row=2, column=0, pady=5)
pass_entry = Entry(window, font=('Arial', 14), width=30)
pass_entry.grid(row=2, column=1, pady=5)

text_sub = Label(window, text='Тема сообщения:', font=('Arial', 14))
text_sub.grid(row=3, column=0, pady=5)
sub_entry = Entry(window, font=('Arial', 14), width=30)
sub_entry.grid(row=3, column=1, pady=5)

mess_text = Label(window, text='Сообщение:', font=('Arial', 14))
mess_text.grid(row=4, column=0, pady=5)
mess_entry = Text(window, font=('Arial', 14), width=30, height=6)
mess_entry.grid(row=4, column=1, pady=5)

btn = Button(window, text='Отправить', font=(
    'Arial', 14), command=send_message)
btn.grid(row=5, column=1)


window.mainloop()

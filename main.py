import smtplib
from email.message import EmailMessage
from tkinter import *


def send_email():
    sender_email=sender_email_entry.get() # 'Koveshnikova-design@ya.ru'
    recipient_mail=recipient_email_entry.get() #'dvarvarg@gmail.com'
    password=password_entry.get() #'gtmvvsktiwrchqro'
    subject=subject_entry.get() #'Проверка связи!'
    body=body_text.get(1.0,END) #'Привет из программы на Питоне'

    msg=EmailMessage()
    msg.set_content(body)
    msg['Subject']=subject
    msg['From']=sender_email
    msg['To']=recipient_mail

    server=None

    try:
        server = smtplib.SMTP_SSL('smtp.yandex.ru',465)
        server.login(sender_email,password)
        server.send_message(msg)
        result_label.config(text='Письмо отправлено!')
    except Exception as e:
        result_label.config(text=f'Ошибка {e}')
    finally: #выполняется в любом случае
        if server:
            server.quit()


window=Tk()
window.title('Отправка Email')
window.geometry('500x300')

Label(text='Отправитель:').grid(row=0,column=0, sticky=W)
sender_email_entry=Entry()
sender_email_entry.grid(row=0,column=1, sticky=W)

Label(text='Получатель:').grid(row=1,column=0, sticky=W)
recipient_email_entry=Entry()
recipient_email_entry.grid(row=1,column=1, sticky=W)

Label(text='Пароль приложения:').grid(row=2,column=0, sticky=W)
password_entry=Entry()
password_entry.grid(row=2,column=1, sticky=W)

Label(text='Тема письма:').grid(row=3,column=0, sticky=W)
subject_entry=Entry()
subject_entry.grid(row=3,column=1, sticky=W)

Label(text='Сообщение:').grid(row=4,column=0, sticky=W)
body_text=Text(width=45,height=10)
body_text.grid(row=4,column=1, sticky=W)

Button(text='Отправить письмо', command=send_email).grid(row=5,column=1, sticky=W)

result_label=Label(text='')
result_label.grid(row=6,column=1, sticky=W)

window.mainloop()

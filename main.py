import smtplib
from email.message import EmailMessage
from tkinter import *


def save():
    with open('save.txt','w') as file:
        file.write(sender_email_entry.get()+'\n')
        file.write(recipient_email_entry.get()+'\n')
        file.write(password_entry.get()+'\n')


def load():
    try:
        with open('save.txt','r') as file:
            info=file.readlines()
            sender_email_entry.insert(0,info[0])
            recipient_email_entry.insert(0,info[1])
            password_entry.insert(0,info[2])
    except FileNotFoundError:
        pass # проигнорировать ошибку


def send_email():
    save()
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
window.geometry('500x400')

Label(text='Отправитель:',font=('Arial',12)).grid(row=0,column=0, sticky=W,pady=3)
sender_email_entry=Entry(width=30)
sender_email_entry.grid(row=0,column=1, sticky=W,pady=3)

Label(text='Получатель:',font=('Arial',12)).grid(row=1,column=0, sticky=W,pady=3)
recipient_email_entry=Entry(width=30)
recipient_email_entry.grid(row=1,column=1, sticky=W,pady=3)

Label(text='Пароль приложения:',font=('Arial',12)).grid(row=2,column=0, sticky=W,pady=3)
password_entry=Entry(width=30)
password_entry.grid(row=2,column=1, sticky=W,pady=3)

Label(text='Тема письма:',font=('Arial',12)).grid(row=3,column=0, sticky=W,pady=3)
subject_entry=Entry(width=30)
subject_entry.grid(row=3,column=1, sticky=W,pady=3)

Label(text='Сообщение:',font=('Arial',12)).grid(row=4,column=0, sticky=W,pady=3)
body_text=Text(width=40,height=10)
body_text.grid(row=4,column=1, sticky=W,pady=3)

Button(text='Отправить письмо',font=('Arial',12), command=send_email).grid(row=5,column=1, sticky=W,pady=3)

result_label=Label(text='',font=('Arial',12))
result_label.grid(row=6,column=1, sticky=W,pady=3)

load()

window.mainloop()

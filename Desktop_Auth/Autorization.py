from tkinter import Tk, CENTER, Label, Entry, Button
from tkinter import messagebox


window = Tk()
window.title('Авторизация')
window.geometry('450x230')
window.resizable(False, False)
font_header = ('TimesNewRoman', 15)
font_entry = ('TimesNewRoman', 12)
label_font = ('TimesNewRoman', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


def userinfo_things(username_entry=None, password_entry=None):
    username = username_entry.get()
    password = password_entry.get()
    messagebox.showinfo('Заголовок', '{username}, {password}'.format(
        username=username, password=password))
    main_label = Label(window, text='Авторизация', font=font_header,
                       justify=CENTER, **header_padding)
    main_label.pack()
    username_label = Label(window, text='Имя пользователя', font=label_font,
                           **base_padding)
    username_label.pack()
    username_entry = Entry(window, bg='#fff', fg='#4A67F7', font=font_entry)
    username_entry.pack()
    password_label = Label(window, text='Пароль', font=label_font,
                           **base_padding)
    password_label.pack()
    password_entry = Entry(window, bg='#fff', fg='#4A67F7', font=font_entry)
    password_entry.pack()


def clicked():
    send_btn = Button(window, text='Войти', command=clicked)
    send_btn.pack(**base_padding)


window.mainloop()

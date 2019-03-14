from tkinter import *
from tkinter import messagebox
from gui.db.check_login import check_login


def check(event):
    login = entry_login.get()
    password = entry_pass.get()
    check_login(login, password)
    

root = Tk()
root.title("Парсер")
label_login = Label(root, text="Введите свой логин: ")
label_pass = Label(root, text="Введите свой пароль: ")
label_copy = Label(root, text="Created by JlecHou6paT", font=5)
entry_login = Entry(root)
entry_pass = Entry(root)
button_check = Button(root, text="Вход", width=15)
label_copy.grid(row=3, column=0)
button_check.grid(row=2, column=1)
button_check.bind("<Button-1>", check)
label_login.grid(row=0, column=0)
label_pass.grid(row=1, column=0)
entry_login.grid(row=0, column=1)
entry_pass.grid(row=1, column=1)

root.mainloop()

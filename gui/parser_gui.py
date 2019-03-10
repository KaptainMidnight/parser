from tkinter import *
from gui import connection


def check_login(event):
    connect = connection.getConnect()
    login = entry_login.get()
    password = entry_pass.get()
    try:
        with connect.cursor() as cursor:
            result = cursor.execute(f"SELECT * FROM users WHERE login={login} AND password={password}")
            if result == 1:
                print("Welcome")
            else:
                print("Error, password is invalid")
    finally:
        connect.close()



root = Tk()
root.title("Мое первое приложение")
label_login = Label(root, text="Введите свой логин: ")
label_pass = Label(root, text="Введите свой пароль: ")
entry_login = Entry(root)
entry_pass = Entry(root)
button_check = Button(root, text="Вход", width=20)
button_check.grid(row=2, column=1)
button_check.bind("<Button-1>", check_login)
label_login.grid(row=0, column=0)
label_pass.grid(row=1, column=0)
entry_login.grid(row=0, column=1)
entry_pass.grid(row=1, column=1)

root.mainloop()

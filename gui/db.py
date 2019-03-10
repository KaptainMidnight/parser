from gui import connection


def check_login(event, entry_login, entry_pass):
    connect = connection.getConnect()
    try:
        login = entry_login.get()
        password = entry_pass.get()
        with connect.cursor() as cursor:
            result = cursor.execute(f"SELECT * FROM users WHERE login={login} AND password={password}")
            print(result)
            if result == 1:
                print("Welcome")
            else:
                print("Error, password is invalid")
    finally:
        connect.close()

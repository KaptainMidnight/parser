from gui.db.connection import get_connect


def check_login(login, passw):
    connect = get_connect()
    try:
        with connect.cursor() as cursor:
            result = cursor.execute(f"SELECT * FROM users WHERE login={login} AND password={passw}")
            row = cursor.fetchone()
            if result == 1 and row['login'] == login and row['password'] == passw:
                print("Успешный вход")
            else:
                print("Неверный логин или пароль")
    finally:
        connect.close()

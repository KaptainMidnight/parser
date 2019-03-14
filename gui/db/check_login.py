from gui.db.connection import get_connect


def check_login(login, passw):
    connect = get_connect()
    try:
        with connect.cursor() as cursor:
            result = cursor.execute(f"SELECT * FROM users WHERE login={login} AND password={passw}")
            if result == 1:
                return "Успешный вход"
            else:
                return "Неверный логин или пароль"
    finally:
        connect.close()

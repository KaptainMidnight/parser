import pymysql


def get_connect():
    connection = pymysql.Connect(
        host="localhost",
        user="root",
        password="adminroot",
        db="gui",
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

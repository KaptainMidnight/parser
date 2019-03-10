import pymysql.cursors


def getConnect():
    connection = pymysql.Connect(
        host="localhost",
        user="root",
        password="adminroot",
        db="gui",
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

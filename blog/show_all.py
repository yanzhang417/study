import pymysql


def load_all_from_mysql():
    connect = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        db='pythonclass',
        charset='utf8'
    )
    cursor = connect.cursor()
    # cursor.execute('show tables')
    sql = "select * from  xxxx"
    cursor.execute(sql)
    return cursor.fetchall()


load_all_from_mysql()

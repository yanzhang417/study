import pymysql


def load_one_from_mysql(id):
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
    sql = "select * from  xxxx where id = %s" % id
    cursor.execute(sql)
    # print(cursor.fetchone())
    return cursor.fetchone()



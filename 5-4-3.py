import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='python', password='1234',
                       db='python_app1', charset='utf8') #autocommit=True

try:
    with conn.cursor() as c:
        #데이터 수정1
        c.execute("UPDATE users SET username = %s WHERE id = %s", ('niceman', 1))
        #데이터 수정2
        c.execute("UPDATE users SET username = '%s' WHERE id = '%d'" % ('goodboy', 2))

        #중간데이터 확인1
        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in c.fetchall():
            print('check1 >',row)

        #데이터 삭제1
        c.execute("DELETE FROM users WHERE id = %s", (1,))
        #데이터 삭제2
        c.execute("DELETE FROM users WHERE id = '%d'" % (2,))

        #중간데이터 확인2
        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in c.fetchall():
            print('check2 >',row)

    conn.commit()
finally:
    conn.close()

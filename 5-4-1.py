#mysql 설치 & 환경변수 등록
#https://dev.mysql.com/downloads/installer/

#mysql -u root -p
#show databases
#use musql
#create user python@localhost identified by '****'
#grant all privileges on db.table to python@localhost
#flush privileges
#exit

#mysql -u python -p
#create database python_app1

#쿼리박스 설치
#http://www.querybox.com/download/

import pymysql
import simplejson as json
import datetime

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='python', password='1234',
                       db='python_app1', charset='utf8') #autocommit=True

#pyMysql 버전확인
print('pymysql.version : ',pymysql.__version__)

#데이터베이스 선택
conn.select_db('DB명')

#Cursor연결
c = conn.cursor()
print(type(c))

#데이터베이스 생성
c.execute('create database python_app2') #DDL, DML, DCL 사용 가능

#커서 반환
c.close()

#접속 해제
conn.close()

#트랜잭션 시작
conn.begin()

#커밋
conn.commit()

#롤백
conn.rollback()

#날짜 생성
now = datetime.datetime.now()
print('now',now)
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S') #2018-08-31 18:21:32
print('nowDatetime',nowDatetime)


#테이블 생성(데이터 타입 : 공식 레퍼런스 참조 또는 검색 참조)
c.execute("CREATE TABLE IF NOT EXISTS users(id bigint(20) NOT NULL, \
                                            username varchar(20) NOT NULL, \
                                            email varchar(30),  \
                                            phone varchar(30), \
                                            website varchar(30), \
                                            regdate varchar(20) NOT NULL, PRIMARY KEY(id))" \
                                            ) #default, AUTO_INCREMENT
#sql = '''
#
#      '''
#c.exectue(sql)

conn.commit()


#JSON to MySQL 삽입1
try:
    with conn.cursor() as c:
        #JSON to MySQL 삽입1
        with open('D:/Atom_Workspace/section5/users.json','r') as infile:
            r = json.load(infile)
            userData = []
            for user in r:
                t = (user['id'], user['username'], user['email'], user['phone'], user['website'], nowDatetime)
                userData.append(t)
            c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (%s, %s, %s, %s, %s, %s)", userData)
            #c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (%s, %s, %s, %s, %s, %s)", tuple(userData))
    conn.commit()
finally:
    conn.close()


try:
    with conn.cursor() as c:
        #JSON to MySQL 삽입2
        with open('D:/Atom_Workspace/section5/users.json','r') as infile:
            r = json.load(infile)
            for user in r:
                c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (%s, %s, %s, %s, %s, %s)", (user['id'], user['username'], user['email'], user['phone'], user['website'], nowDatetime))
        #테이블 Row 삭제
        print("users db deleted : ", c.execute("delete from users"), "rows")
    conn.commit()
finally:
    conn.close()

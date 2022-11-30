# test.py

import oracledb


with oracledb.connect(user='dbanalytics', password='dbanalytics', dsn='localhost/xe') as connection:
    with connection.cursor() as cursor:
        sql = """select sysdate from dual"""
        for r in cursor.execute(sql):
            print(r)
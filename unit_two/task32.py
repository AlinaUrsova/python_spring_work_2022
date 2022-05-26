# todo: Написать скрипт создания базы данных(ER-модели) TestSystem
# Скрипт  create_db.py  должен создавать таблицы, индексы , констрейнты в СУБД PostgresSQL
# В задании использовать библиотеку psycopg


#Ссылка на документацию
#https://www.psycopg.org/psycopg3/docs/basic/usage.html
#Для подключения использовать пользователя и базу отличную от postgres


#см. файл create_db.py

import psycopg

with psycopg.connect("dbname=my_test user=my_user_test password=123") as conn:
    with conn.cursor() as cur:
        # создание таблиц
        cur.execute("""CREATE TABLE "my_test_group" (
                  "group" SERIAL PRIMARY KEY,
                  "name" VARCHAR(100)
                    );""")

        #cur.execute("""
            CREATE TABLE "my_test_student" (
               "id_student" serial PRIMARY KEY,
               "id_group" integer not null,
               "name" varchar(100),
               "age" int)
            """)

        # создание индекса
        cur.execute(
                 """CREATE INDEX "idx_my_test_student__id_group" ON "my_test_student" ("id_group");""")

        #создание констрейн

        #cur.execute("""
                 ALTER TABLE "my_test_student" ADD CONSTRAINT "fk_my_test_student_id_group" FOREIGN KEY ("id_group")
                REFERENCES "my_test_group" ("group")
                 """)

        #новая запись в таблицу

        cur.execute("""
                 INSERT INTO "my_test_group" ("group", name)
                 VALUES (1,'group_3');
                 """)

        cur.execute("""
                   INSERT INTO "my_test_student" (id_student, id_group, name, age )
                   VALUES (1, 1, 'Ivan', 27);
                   """)


        
        cur.execute("SELECT * FROM test")
        cur.fetchall()

        for record in cur:
            print(record)

        conn.commit()
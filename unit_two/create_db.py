import psycopg

with psycopg.connect("dbname=my_test user=my_user_test password=123") as conn:
    with conn.cursor() as cur:

#Создание таблиц
        #cur.execute("""
        #    CREATE TABLE "group" (
        #        "id_group" serial PRIMARY KEY,
        #        "name_group" varchar(100))
        #    """)
        #cur.execute("""
        #    CREATE TABLE "student" (
        #       "id_student" serial PRIMARY KEY,
        #       "id_group" integer not null,
        #       "name" varchar(100)
        #       "age" int)
        #    """)


        # Query the database and obtain data as Python objects.
        cur.execute("SELECT * FROM test")
        cur.fetchone()

        for record in cur:
            print(record)

        conn.commit()
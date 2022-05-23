#todo: Написать авторизацию пользователя в систему.
#Приложение в начале должно предлагать меню
#1. Вход
#2. Регистрация


#1. При выборе пункта "Вход" пользователю необходимо ввести
#логин и пароль, поэтапно.
#login: _________
#password: ________
#При вводе данных авторизации, система проверяет есть ли данный
#пользователь в БД (логин) если нет то предлагает зарегистрироваться.
#Если есть и пароли совпадают, то происходит вход в систему. Пользователю показывается
#приглашение вида "Добро пожаловать Вася Пупкин!" и выпадает меню
#выбора билетов для тестирования(пока заглушка).

#2. При выборе "Регистрация" пользователю необходимо ввести новый
#логин, пароль, фио, почту, телефон, группу. После система заводит
#запись в БД если пользователя под данным логином нет. Если такой пользователь
#уже существует то программа выдает об этом сообщение. Пароль необходимо хранить в БД
#в виде хеша + соль.

#По хешированию прочитать статью
#https://pythonist.ru/heshirovanie-parolej-v-python-tutorial-po-bcrypt-s-primerami/
#для хеширования пароля воспользоваться библиотекой bcrypt
import time
import psycopg
#import bcrypt

#пока без зашифровки пароля

def login_password():
    with psycopg.connect("dbname=my_test user=my_user_test password=123") as conn:
        with conn.cursor() as cur:
            print_login = str(input('Введите логин: '))
            cur.execute(f"""SELECT login, password FROM user_lp where login = '{print_login}'""")
            login_password_select = cur.fetchone()
            login_select = login_password_select[0]
            password_select = login_password_select[1]
            if login_select is None:
                print('Пользователь не найден. Хотите зарегистрироваться?')
            else:
                print_password = str(input('Введите пароль: '))
                if print_password == password_select:
                    cur.execute(f"""SELECT fio FROM user_lp where login = '{print_login}'""")
                    fio_select = cur.fetchone()

                    print("Добро пожаловать,", *fio_select)
                else:
                    print("Пароль неверный, попробуйте еще раз")
                    return(login_password())
        conn.commit()


def registration():
    with psycopg.connect("dbname=my_test user=my_user_test password=123") as conn:
        with conn.cursor() as cur:
            print("Регистрация нового пользователя")

            try:
                new_login = str(input("Введите логин: "))
                cur.execute(f"""SELECT login FROM user_lp where login = '{new_login}'""")
                new_login_select = cur.fetchone()
                if new_login == new_login_select[0]:
                    print("Логин занят. Пожалуйста, введите другой логин")

            except:

                new_password = str(input("Введите пароль: "))
                new_surname = str(input("Введите фамилию: "))
                new_name = str(input("Введите имя: "))
                new_patronymic = str(input("Введите отчество: "))
                new_fio = new_surname + " " + new_name + " " + new_patronymic
                new_age = int(input("Введите возраст: "))
                new_data = str(time.ctime())
                new_mail = str(input("Введите почту: "))
                new_phone = int(input("Введите номер телефона: "))
                new_group = int(input("Введите номер группы: "))
                cur.execute("select id_user from user_lp")
                ids = cur.fetchall()
                id_new = (len(ids)) + 1
                cur.execute("insert into user_ values (%s, %s, %s, %s, %s, %s, %s)",
                        [id_new, new_surname, new_name, new_patronymic, new_age, new_data, True])
                cur.execute("insert into user_lp values (%s, %s, %s, %s, %s, %s, %s, %s)",
                        [id_new, id_new, new_login, new_password, new_fio, new_mail, new_phone, new_group])
                print("Регистрация завершена, можете войти в систему")

        conn.commit()

def test_student():
    pass

print("Добро пожаловать! Выберите действие:\n"
                   "1. Войти.\n"
                   "2. Зарегистрироваться.\n")

action = int(input("Нажмите:"))
if action == 1:
    login_password()
if action == 2:
    registration()













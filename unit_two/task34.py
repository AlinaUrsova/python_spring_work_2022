#todo: Реализовать классы DB и Profile

#class DB:
#    '''Данный класс содержит конструктор и метод get_connect. В конструкторе инициализируются переменные
#     (атрибуты доступа к БД) . Метод возвращает соединение.'''
#    __init__(self, dbname, user, password):
#        # В констукторе инициализируем атрибуты доступа к БД
#        pass
#    def get_connect(self):
#        # Метод возвращает соединение к БД
#        pass



#class Profile:
#    ''' Данный класс содержит конструктор и метод set_profile и get_profile для добавления и получения
#     пользователя соответсвенно'''
#
#   # В констукторе инициализируем атрибуты сущности Profile
#    __init__(self, login, password, name, surname, age, tel, email):
#        pass

#    # в аргументе conn передается дискриптор подключения к БД
#    def set_profile(self, conn):
#        # Добавляет профиль в БД
#        pass
#
#    def get_profile(self, conn):
#        # Извлекает профиль из БД
#        pass



import psycopg
class Db:
    def __init__(self, dbname, user, password):
        self.dbname = dbname
        self.user = user
        self.password = password
    def getconnection(self):
        conn = psycopg.connect(f"dbname={self.dbname} user={self.user} password={self.password}")
        return conn

class Profile:
    def __init__(self, db, login, password, name, surname, phones, age):
        self.db = db
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.phones = phones
        self.age = age

    def getprofile(self):
        cur = conn.cursor()
        cur.execute(f"""SELECT login FROM user_lp where login = '{self.login}'""")
        res_login = cur.fetchall()
        return res_login

    def setprofile(self):
        cur = conn.cursor()
        cur.execute(f"INSERT INTO test3 (login, password, name, surname, phones, age) VALUES "
                    f"('{self.login}', '{self.password}', '{self.name}', '{self.surname}', {self.phones}, {self.age});")
        conn.commit()



conn = Db("my_test", "my_user_test", "123")
conn = conn.getconnection()



new_student = Profile("my_test", "admin", "123", "Ivanov", "Ivanivich", 899999999, 19)
new_student.setprofile()

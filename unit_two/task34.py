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


conn = Db("my_test", "my_user_test", "123")
conn = conn.getconnection()
print(conn)

class Profile:
    def __init__(self, db, login_u, password_u, fio, mail, phones, group):
        self.db = db
        self.login_u = login_u
        self.password_u = password_u
        self.fio = fio
        self.mail = mail
        self.phones = phones
        self.group = group
        #self.conn = conn
    def getprofile(self):
        #conn = psycopg.connect(f"dbname={self.name} user={self.user} password={self.password}")
        get_login = conn.execute(f"""SELECT login FROM user_lp where login = '{self.login_u}'""")
        #res_login = conn.fetchall()
        return get_login

    # часть с setprofile не сделала еще
    def setprofile(self):
        #conn = psycopg.connect(f"dbname={self.name} user={self.user} password={self.password}")
        conn.execute("select id_user from user_lp")
        ids = conn.fetchall()
        id_new = (len(ids)) + 1
        conn.execute(f"""insert into user_ values ({id_new}, '{self.} """)

conn_profile = Profile("my_test", "admin", "123", "Ivanov Ivan Ivanovich", "mail@mail.ru", "899999999", "1")
get1 = conn_profile.getprofile()
print(get1)
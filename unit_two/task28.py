#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
#Пример:
#render, 10,  12.05.2022 12:00
#show,    5,  12.05.2022 12:02
#render, 15,  12.05.2022 12:07

#Декоратор должен применяться для различных функций с переменным числом аргументов.
#Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

import time
import random

def decoration_(func):
    def wrapper(*args):
        f = open('debug.log', 'a+', encoding='utf-8')
        start_func = func(*args)
        wrapper.count += 1
        log = str(func.__name__) + " " + str(wrapper.count) + " " + str(time.ctime())
        f.write(str(log))
        f.write('\n')
        print(str(log))
        return start_func
    wrapper.count = 0
    return wrapper


@decoration_

def render(*args):
    sum_ = sum(*args)
    print(sum_)


n = random.sample(range(0, 1000000), 50000)
render(n)


@decoration_
def show(*args):
    print(*args)

text = ("Hi")
show(text)

render(n)

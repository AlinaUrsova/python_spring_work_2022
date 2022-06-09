# todo: Прасим страницу сайта центробанка
# Зайдите на сайт Центробанка(cbr.ru) через http-client
# Получите индексную страницу.
# Из индексной страницы извлеките данные по: ключевой ставки, курсе валюты USD, EUR
# Выведите полученные данные на консоль


import http.client
conn = http.client.HTTPSConnection("www.cbr.ru")
conn.request("GET", "/")
# Получить ответ сервера
response = conn.getresponse()
# Получить заголовки сервера
headers = response.getheaders()

print(response.status, response.reason)

data = response.read().decode('UTF-8')

with open("cbr_ru.json", 'w', encoding='UTF-8') as file:
    file.write(data)

with open("cbr_ru.json", 'r', encoding='UTF-8') as file:
    key = file.readlines()
    for i in range(len(key)):
        if "Ключевая ставка" in key[i]:
            print('Ключевая ставка', key[i + 4][9:21], key[i + 8][38:44])
    for i in range(len(key)):
        if "Курсы валют" in key[i]:
            print('Курс USD:', key[i + 4][118:128], key[i + 16][55:65])
    for i in range(len(key)):
        if "Курсы валют" in key[i]:
            print('Курс EUR:', key[i + 4][118:128], key[i + 32][55:65])

conn.close()
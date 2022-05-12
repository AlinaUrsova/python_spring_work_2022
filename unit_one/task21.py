# todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html

#page = {"title": "Тег BODY",
#        "charset": "utf-8",
#        "alert": "Документ загружен",
#        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}

#template = """
#<!DOCTYPE HTML>
#<html>
# <head>
#  <title> ? </title>
#  <meta charset=?>
# </head>
# <body onload="alert(?)">

#  <p>?</p>

# </body>
#</html>
#"""

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}

file = open('index.html', 'r+')
lines = file.readlines()
new_lines = list()

for i in lines:
    for key in page:
        if key in lines:
            num = i.find("?")
            new_lines.append(str(i[:num]) + str(page[key]) + str(i[num + 1:]))
            break
    else:
        new_lines.append(i)

print(*new_lines)
f = open("index.html", "w")
f.writelines(new_lines)
f.close()

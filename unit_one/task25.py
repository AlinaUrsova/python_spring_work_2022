#todo: Убрать повторяющиеся буквы и лишние символы
#Построить по ключевой фразе часть алфавита. Взять все буквы по одному разу. Не буквы убрать.
#Буквы должны идти в том порядке, в котором встретились во фразе в первый раз.

#Input             	            Output
#apple	                        aple
#25.04.2022 Good morning !!	    godmrni



text = input("Введите текст: ")
alf = str()

for element in text.lower():
    if element.isalpha():
        if element in alf:
            continue
        else:
            alf += element
    else:
        continue
print(alf)

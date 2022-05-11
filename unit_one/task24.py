#todo: Числа в буквы
#Замените числа, написанные через пробел, на буквы. Не числа не изменять.

#Пример.
#Input	                            Output
#8 5 12 12 15	                    hello
#8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

alfavit = "abcdefghijklmnopqrstuvwxyz"
text = input("Введите строку: ")
out_text = []

for i in text.split(" "):
    encrypted = ""
    if i.isdigit() == True:
        if int(i) == 0:
            encrypted += (" ")
        else:
            encrypted = (alfavit[int(i) - 1]) + encrypted
    else:
        encrypted += i
    out_text.append(encrypted)

print(*out_text)


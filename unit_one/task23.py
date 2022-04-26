#todo: Взлом шифра
#Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
#Попробуйте все возможные сдвиги и расшифруйте фразу.


#grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

alfavit =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin".upper()
print("текст который нужно расшифровать: ", message)
smeshenie = int(input('Шаг шифровки: '))

itog = ''
for i in message:
        mesto = alfavit.find(i)
        new_mesto = mesto - smeshenie
        if i in alfavit:
            itog += alfavit[new_mesto]
        else:
            itog += i
print("расшифровка: ", itog)

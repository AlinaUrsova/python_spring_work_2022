#todo: Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.

#Пример:
#mass = [1,2,17,16,30,51,2,70,3,2]

#Для числа 2 индексы двух ближайших чисел: 6 и 9

#Пример:
#mass = [1,2,17,54,30,89,2,1,6,2]
#Для числа 1 индексы двух ближайших чисел: 0 и 7
#Для числа 2 индексы двух ближайших чисел: 6 и 9

mass = []
masi = []
index = 0
N = int(input("введите размер массива"))
for i in range(N):
    mass.append(int(input("введите элемент массива")))
print(mass)
for i in mass:
    if mass.count(i) >= 2:
        #не понимаю как вывести несколько индексов
        #while i < N:
            #i = mass.index(i)
            #masi.append(i)
            #index = i + 1
    #print(masi)




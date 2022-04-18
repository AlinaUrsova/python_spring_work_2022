#todo: Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.

#Пример:
#mass = [1,2,17,16,30,51,2,70,3,2]

#Для числа 2 индексы двух ближайших чисел: 6 и 9

#Пример:
#mass = [1,2,17,54,30,89,2,1,6,2]
#Для числа 1 индексы двух ближайших чисел: 0 и 7
#Для числа 2 индексы двух ближайших чисел: 6 и 9

#mass = [1, 2, 3, 2, 0]
#masi = []
mass = []
N = int(input("введите размер массива"))
for i in range(N):
    mass.append(int(input("введите элемент массива")))
print(mass)
x = 0
for i in mass:
    if mass.count(i) >= 2:
        x = i
position = 0
start = 0
index_for_element = []
length = len(mass)
while position < length:
    i = mass.index(x, position)
    index_for_element.append(i)
    position = i + 1
print(index_for_element)
start = None
min_ = 1000000
for elm in index_for_element:
    if start is None:
        start = elm
        continue
    if elm - start < min_:
        min_ = elm - start
        first_start_index = start
        second_start_index = elm
print(first_start_index)
print(second_start_index)




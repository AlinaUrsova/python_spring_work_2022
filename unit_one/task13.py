#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

mass = []
N = 10
for i in range(N):
    mass.append(int(input("введите элемент массива")))
print(mass)
for i in range(N):
    mass[i] += 1
print(mass)

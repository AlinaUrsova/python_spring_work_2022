# todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().

a = int(input('введите точку а'))
b = int(input('введите точку b'))
c = int(input('введите точку c'))
ac = c-a
print('AC-',ac)
bc = c-a
print('BC-',bc)
print('сумма-',ac+bc)
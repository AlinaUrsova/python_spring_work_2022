#todo: Найти сумму элементов матрицы,
#Написать msum(matrix)  которая подсчитывает сумму всех элементов функцию Найти сумму всех элементов матрицы:

#>>> matrix = [[1, 2, 3], [4, 5, 6]]
#>>> msum(matrix)
#21

#>>> msum(load_matrix('matrix.txt'))
#423

def msum(matrix):
    n = [x for i in matrix for x in i]
    return sum(n)

matrix = [[1, 2, 3], [4, 5, 6]]

print(f"Исходная матрица {matrix}")
print(f"Сумма всех элементов матрицы {msum(matrix)}")
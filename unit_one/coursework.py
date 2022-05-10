#todo: III вариант (пирамидальная сортировка )
#Реализовать на Python пирамидальную сортировку представленную в псевдокоде
#в учебнике “Introduction to Algorithms”  на стр. 178 - 184.

#Задача.
#Перепишите процедуру  MAX_HEAPIFY и напечатайте получившеестся бинарное дерево
#при входном списке A = [50, 14, 60, 7, 20, 70, 55, 5, 15, -10]


def parent(i):
    return i//2

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

def max_heapify(A,i):
    l = left(i)
    r = right(i)
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A):
    n = int((len(A)//2)-1)
    for i in range(n, -1, -1):
        max_heapify(A,i)

A = [50, 14, 60, 7, 20, 70, 55, 5, 15, -10]
build_max_heap(A)
print(A)
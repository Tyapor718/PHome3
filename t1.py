# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой 
# строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
from random import randint
from collections import Counter
N= int (input ('Введите N '))
X= int (input ('Введите X '))
a=[randint (1,5) for i in range (N)]
s=0
for i in range (N):
       print (a[i], end= ' ')
for i in range (N):
    if a[i]==X:
        s+=1
if s!=0:
    print ('Число в массиве', s, 'раз' )
else:
    print ('нет числа в массиве')
    
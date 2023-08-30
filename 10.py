
"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть"""

from random import randint
n = (int(input("Введите количество монет:")))
orel = 0
reschka = 0
for i in range(n):
    money = randint(0, 1)
    print(money, end='')
    if money == 0:
       reschka += 1
    elif money==1:
         orel += 1
print()
if orel < reschka:
       print(orel)
else:
       print(reschka)
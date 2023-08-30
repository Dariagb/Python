"""Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа."""

from math import sqrt
summa = (int(input("Введите сумму:")))
proisvedenie = (int(input("Введите произведение:")))
res = sqrt((summa/2)**2 - proisvedenie)
first_number = int(summa/2 - res)
second_number = int(summa/2 + res)
print(first_number, second_number)

"""Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24."""

from itertools import count
from math import factorial

# Вариант 1
def fact(n):
    fact = 1
    for x in range(1, n+1):
        fact = fact * x
        yield(fact)

# Вариант 2

def fact(n):
    fact = 1
    for x in count(1):
        if x > n:
            break
        fact = fact * x
        yield(fact)

# Вариант 3

def fact(n):
    for x in count(1):
        if x > n:
            break
        yield(factorial(x))


for el in fact(6):
    print(el)


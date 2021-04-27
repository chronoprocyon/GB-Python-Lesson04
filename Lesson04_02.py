"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
import random

numbers_list = [x for x in range(1, 20)]

random.shuffle(numbers_list)

new_list = []
temp_el = numbers_list[0]
int(temp_el)

for el in numbers_list:
    int(el)
    if el > temp_el:
        new_list.append(el)
    temp_el = el

print(numbers_list)
print(new_list)

"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

import sys

try:
    name, salperhour, hour, bonus = sys.argv
except ValueError:
    print("Invalid Args")
    exit()


def calculate(salperhour, hour, bonus):
    try:
        salperhour = float(salperhour)
        hour = float(hour)
        bonus = float(bonus)
        print((salperhour * hour + bonus) * 0.87)
    except ValueError:
        print("Please enter only numbers")


calculate(salperhour, hour, bonus)

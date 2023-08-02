# -*- coding: utf-8 -*-
"""
Завдання 7.3b

Створити копію скрипта завдання 7.3a.

Переробити скрипт:
* запросити користувача ввести номер VLAN
* виводити інформацію лише за вказаним VLAN

Приклад роботи скрипта:
$ python task_7_3b.py
Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

"""

template = "{:9}{:20}{}"
input_vlan = input('Enter VLAN number: ')

with open('CAM_table.txt') as file:
    var = file.readlines()
mid = []
for i in var:
    unit = i.split()
    if len(unit)==4 and unit[0].isdigit():
        mid.append([unit[0],unit[1],unit[-1]])

for i in mid:
    if i[0] == input_vlan:
        print(template.format(*i))
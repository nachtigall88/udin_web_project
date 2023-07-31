# -*- coding: utf-8 -*-
"""
Завдання 7.1

Обробити рядки з файлу ospf.txt і вивести інформацію щодо кожного рядка в
такому вигляді на стандартний потік виводу:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

"""
template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""

with open('ospf.txt', 'r') as file:
    mid = file.readlines()

mid = [''.join(x.split('via')) for x in mid]
mid = [''.join(x.split(','))[:-1] for x in mid]
mid = [x.split(' ') for x in mid]
for x in mid:
    while '' in x:
        x.remove('')
mid = [[x.lstrip('[').rstrip(']') for x in y] for y in mid]

for i in mid:
    print(template.format(*i[1:]))

# print(mid)

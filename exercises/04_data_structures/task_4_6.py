# -*- coding: utf-8 -*-
from pprint import pprint
"""
Завдання 4.6

Обробити рядок ospf_route та вивести інформацію на стандартний потік виведення у вигляді:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Для цього використовувати шаблон template і підставити значення з рядка
ospf_route. Значення рядка ospf_route треба отримати за допомогою Python.

Попередження: у розділі 4 тести можна легко "обдурити", зробивши потрібний
вивід print, без отримання результатів з даних завдання за допомогою Python. Це
не означає, що завдання зроблено правильно, просто на даному етапі складно
інакше перевіряти результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_route = ospf_route.strip()
ospf_route = ''.join(ospf_route.split('via '))
ospf_route = ''.join(ospf_route.split(','))
ospf_route = ospf_route.replace('[', '').replace(']', '')
# print(ospf_route)
res = ospf_route.split()
template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""
# pprint(template.format(*res))
print(template.format(*res))

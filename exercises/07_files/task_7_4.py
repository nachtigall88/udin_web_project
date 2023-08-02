# -*- coding: utf-8 -*-
"""
Завдання 7.4

Створити скрипт, який оброблятиме конфігураційний файл комутатора і
отримуватиме з нього інформацію про порти в режимі trunk і вланах, які
налаштовані на цих портах.

Ім'я конфігураційного файлу передається як аргумент скрипту.
$ python task_7_4.py config_trunk_sw2.txt
$ python task_7_4.py config_trunk_sw3.txt

Передавати ім'я файлу як аргумент скрипту. Вказаний конфіг потрібно обробити і
отримати словник портів у режимі trunk, де ключі номери портів, а значення
список дозволених VLAN (список рядків).

Записати підсумковий словник у змінну trunk_dict (саме ця змінна
перевірятиметься у тесті). За бажанням можна виводити словник на екран, тест
перевіряє лише вміст змінної. Тут зручно виводити словник за допомогою pprint.

Наприклад, для файлу config_trunk_sw2.txt повинен вийти такий словник:
$ python task_7_4.py config_trunk_sw2.txt
{'FastEthernet0/1': ['100', '200'],
 'FastEthernet0/3': ['100', '300', '400', '500', '600'],
 'FastEthernet0/4': ['400', '500', '600']}

Для файлу config_trunk_sw3.txt повинен вийти такий словник:
$ python task_7_4.py config_trunk_sw3.txt
{'FastEthernet0/1': ['10', '20', '21', '22'],
 'FastEthernet0/2': ['10', '13', '1450', '1451', '1452'],
 'FastEthernet0/6': ['40', '50', '60']}

Перевірити роботу функції на прикладі файлів config_trunk_sw2.txt та
config_trunk_sw3.txt. Переконайтеся, що в результаі для цих файлів виходять
вірні словники.

Підказка щодо синтаксису cisco: у цьому завданні вважаємо, що інтерфейс
знаходиться в режимі trunk, якщо в нього налаштована команда:
switchport trunk allowed vlan.
"""
import string
from pprint import pprint
from string import digits

with open('config_trunk_sw2.txt') as file_2:
    # for i in file_2:
    #     print(i)
    mid_file = []
    for i in file_2:
        if 'interface' in i or 'trunk allowed vlan' in i:
            mid_file.append(i)
    res_file = []
    for i in range(len(mid_file)):
        if 'trunk allowed vlan' in mid_file[i]:
            res_file.append((mid_file[i - 1], mid_file[i]))
    res_file = [(x[0][:-1], x[1][:-1]) for x in res_file]
    res_file = [(x[0].split()[-1], x[-1].split()[-1]) for x in res_file]
    trunk_dict = {}
    for i in res_file:
        trunk_dict[i[0]] = i[-1].split(',')
    # print([*file_2])
    # print(mid_file)
    # print(res_file)
    # print(fin_dict)
    # for i in fin_dict.items():
    #     print(*i)
    pprint(trunk_dict)
# -*- coding: utf-8 -*-
"""
Завдання 7.5

Створити скрипт, який оброблятиме конфігураційний файл комутатора і
отримуватиме з нього інформацію про конфігурацію інтерфейсів.

Ім'я конфігураційного файлу передається як аргумент скрипту.
$ python task_7_5.py config_trunk_sw2.txt
$ python task_7_5.py config_trunk_sw3.txt

Передавати ім'я файлу як аргумент скрипту. Вказаний конфіг треба обробити і
отримати словник де ключі ім'я інтерфейсу, а значення список команд, які
починаються на switchport. Команди у списку мають бути без пробілу на початку
рядка та переведення рядка наприкінці.

Записати підсумковий словник у змінну interface_dict (саме ця змінна
перевірятиметься у тесті). За бажанням можна виводити словник на екран, тест
перевіряє лише вміст змінної. Тут зручно виводити словник за допомогою pprint.

Наприклад, для файлу config_trunk_sw2.txt повинен вийти такий словник:

$ python task_7_5.py config_trunk_sw2.txt
{'FastEthernet0/1': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 100,200',
                     'switchport mode trunk'],
 'FastEthernet0/2': ['switchport mode access',
                     'switchport access vlan 20'],
 'FastEthernet0/3': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 100,300,400,500,600',
                     'switchport mode trunk'],
 'FastEthernet0/4': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 400,500,600',
                     'switchport mode trunk'],
 'FastEthernet0/5': ['switchport mode access',
                     'switchport access vlan 30'],
 'FastEthernet0/6': ['switchport mode access',
                     'switchport access vlan 20']}

Для файлу config_trunk_sw3.txt повинен вийти такий словник:
$ python task_7_5.py config_trunk_sw3.txt
{'FastEthernet0/1': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 10,20,21,22',
                     'switchport mode trunk'],
 'FastEthernet0/2': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 10,13,1450,1451,1452',
                     'switchport mode trunk'],
 'FastEthernet0/3': ['switchport mode access',
                     'switchport access vlan 20'],
 'FastEthernet0/4': ['switchport mode access',
                     'switchport access vlan 20'],
 'FastEthernet0/5': ['switchport mode access',
                     'switchport access vlan 30'],
 'FastEthernet0/6': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 40,50,60',
                     'switchport mode trunk'],
 'FastEthernet0/7': ['switchport mode access'],
 'FastEthernet0/8': ['switchport mode access']}

Перевірити роботу функції на прикладі файлів config_trunk_sw2.txt та
config_trunk_sw3.txt. Переконайтеся, що в результаі для цих файлів виходять
вірні словники.

"""
from pprint import pprint
from sys import argv
interface_dict = 'config_trunk_sw2.txt'

if len(argv) == 2:
    interface_dict = argv[1]


with open(interface_dict) as file_2:
    mid_file_2 = []
    res_file_2 = []
    for i in file_2:
        if 'FastEtherne' in i or 'switchport' in i:
            mid_file_2.append(i)
    mid_file_2 = [x[:-1] for x in mid_file_2]
    mid_file_2 = ''.join(mid_file_2)
    mid_file_2 = mid_file_2.split('interface ')[1:]
    mid_file_2 = [(x.split()) for x in mid_file_2]
    mid_file_2 = [(x[0], ' '.join(x[1:])) for x in mid_file_2]
    mid_file_2 = [(x[0], x[-1].replace(' switchport', ', switchport')) for x in mid_file_2]
    mid_file_2 = [(x[0], [x[-1]]) for x in mid_file_2]
    # mid_file_2 = [(x[0], 'switchport'.join(x[-1].split('switchport'))) for x in mid_file_2]
    # mid_file_2 = [(x[0], x[-1].split(',')[1:]) for x in mid_file_2]
    interface_dict = {}
    for i in mid_file_2:
        interface_dict[i[0]] = i[-1]
    # print(mid_file_2)
    pprint(interface_dict)


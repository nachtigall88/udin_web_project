# -*- coding: utf-8 -*-
from pprint import pprint
from string import digits

"""
Завдання 9.6

Створити функцію get_int_vlan_map, яка обробляє конфігураційний файл комутатора
та повертає кортеж із двох словників:
* словник портів у режимі access, де ключі номери портів, а значення access
  VLAN (числа)
* словник портів у режимі trunk, де ключі номери портів, а значення список
  дозволених VLAN (список чисел)

Функція повинна мати один параметр config_filename, який очікує як аргумент
ім'я конфігураційного файлу.

Перевірити роботу функції на прикладі файлу config_sw1.txt

Приклад роботи функції
In [2]: get_int_vlan_map("config_sw1.txt")
Out[2]:
({'FastEthernet0/0': 10,
  'FastEthernet0/2': 20,
  'FastEthernet1/0': 20,
  'FastEthernet1/1': 30},
 {'FastEthernet0/1': [100, 200],
  'FastEthernet0/3': [100, 300, 400, 500, 600],
  'FastEthernet1/2': [400, 500, 600]})

In [3]: access, trunk = get_int_vlan_map("config_sw1.txt")

In [4]: access
Out[4]:
{'FastEthernet0/0': 10,
 'FastEthernet0/2': 20,
 'FastEthernet1/0': 20,
 'FastEthernet1/1': 30}

In [5]: trunk
Out[5]:
{'FastEthernet0/1': [100, 200],
 'FastEthernet0/3': [100, 300, 400, 500, 600],
 'FastEthernet1/2': [400, 500, 600]}


У завданнях 9го розділу і далі, крім зазначеної функції, можна створювати
будь-які додаткові функції.
"""


def make_access_dict(data):
    res_data = {}
    check_str = digits + ','
    k,v = 1,2
    for i in data.split():
        if 'FastEthernet' in i:
            res_data[i] = []
            k = i
        if all(map(lambda x: x in check_str, i)):
            v = int(i)
            res_data[k] = v
    return res_data

def make_tunk_dict(data):
    res_data = {}
    check_str = digits + ','
    for i in data.split():
        if 'FastEthernet' in i:
            res_data[i] = []
            k = i
        if all(map(lambda x: x in check_str, i)):
            v = i
            res_data[k] = [int(x) for x in v.split(',')]
    return res_data

def get_int_vlan_map(config_filename):
    with open(config_filename) as file:
        mid_list = []
        for i in file:
            if '!' not in i and 'interface' in i or 'switchport' in i:
                mid_list.append(i[:-1])
    access_dict = {}
    trunk_dict = {}
    res = ' '.join(mid_list).split('interface')
    for j in res:
        if 'access' in j:
            mid = make_access_dict(j)
            access_dict.update(mid)
        if 'trunk' in j:
            mid = make_tunk_dict(j)
            trunk_dict.update(mid)



    # print(res)
    return access_dict, trunk_dict

    # print(res)
    # print(type(res))


pprint(get_int_vlan_map('config_sw1.txt'))

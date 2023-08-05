# -*- coding: utf-8 -*-
from pprint import pprint
from string import digits
"""
Завдання 9.6a

Зробити копію функції get_int_vlan_map із завдання 9.6.

Доповнити функцію: додати підтримку конфігурації, коли налаштування порту
access виглядає так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

Тобто, порт знаходиться у VLAN 1

У такому випадку до словника портів повинна додаватися інформація, що порт у
VLAN 1. Приклад словника:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

Функція повинна мати один параметр config_filename, який очікує як аргумент
ім'я конфігураційного файлу.

Перевірити роботу функції на прикладі файлу config_sw2.txt
Приклад роботи функції
In [2]: get_int_vlan_map("config_sw2.txt")
Out[2]:
({'FastEthernet0/0': 10,
  'FastEthernet0/2': 20,
  'FastEthernet1/0': 20,
  'FastEthernet1/1': 30,
  'FastEthernet1/3': 1,
  'FastEthernet2/0': 1,
  'FastEthernet2/1': 1},
 {'FastEthernet0/1': [100, 200],
  'FastEthernet0/3': [100, 300, 400, 500, 600],
  'FastEthernet1/2': [400, 500, 600]})

In [4]: access, trunk = get_int_vlan_map("config_sw2.txt")

In [5]: access
Out[5]:
{'FastEthernet0/0': 10,
 'FastEthernet0/2': 20,
 'FastEthernet1/0': 20,
 'FastEthernet1/1': 30,
 'FastEthernet1/3': 1,
 'FastEthernet2/0': 1,
 'FastEthernet2/1': 1}

In [6]: trunk
Out[6]:
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

def add_vlan_1(data_dict):
    for i in data_dict:
        if bool(data_dict[i]) == False:
            data_dict[i] = 1
    return data_dict
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
    access_dict = add_vlan_1(access_dict)


    # print(res)
    return access_dict, trunk_dict
res = get_int_vlan_map('config_sw2.txt')
# pprint(res)
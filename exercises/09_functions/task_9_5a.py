# -*- coding: utf-8 -*-
from pprint import pprint
"""
Завдання 9.5a

Зробити копію функції generate_trunk_config із завдання 9.5

Змінити функцію таким чином, щоб вона повертала не список команд, а словник:
* ключі: імена інтерфейсів, виду 'FastEthernet0/1'
* значення: список команд, який потрібно виконати на цьому інтерфейсі

Перевірити роботу функції на прикладі словника trunk_dict та шаблону
trunk_cmd_list.


Приклад роботи функції
In [2]: pprint(generate_trunk_config(trunk_dict, trunk_cmd_list))
{'FastEthernet0/1': ['switchport mode trunk',
                     'switchport trunk native vlan 999',
                     'switchport trunk allowed vlan 10,20,30'],
 'FastEthernet0/2': ['switchport mode trunk',
                     'switchport trunk native vlan 999',
                     'switchport trunk allowed vlan 11,30'],
 'FastEthernet0/4': ['switchport mode trunk',
                     'switchport trunk native vlan 999',
                     'switchport trunk allowed vlan 17']}

У завданнях 9го розділу і далі, крім зазначеної функції, можна створювати
будь-які додаткові функції.
"""


trunk_cmd_list = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_dict = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

def generate_trunk_config(intf_vlan_dict, trunk_template):
    res_dict = {}
    for i in intf_vlan_dict:
        res_dict[i] = []
        for j in trunk_template:
            if j == 'switchport trunk allowed vlan':
                res_dict[i].append(j+' '+','.join([str(x) for x in intf_vlan_dict[i]]))
            else:
                res_dict[i].append(j)
    return res_dict


# pprint(generate_trunk_config(trunk_dict, trunk_cmd_list))
generate_trunk_config(trunk_dict, trunk_cmd_list)

# -*- coding: utf-8 -*-
"""
Завдання 9.1

Створити функцію convert_mac, яка конвертує MAC-адресу з формату 1a1b.2c2d.3e3f
в 1a:1b:2c:2d:3e:3f.

Функція повинна мати один параметр: mac_address, який очікує рядок з
MAC-адресою у форматі 1a1b.2c2d.3e3f. Функція повинна повертати рядок з
MAC-адресою у форматі 1a:1b:2c:2d:3e:3f.

Перевірити роботу функції на різних MAC-адресах у списку mac_list.

У цьому завданні можна не перевіряти, що MAC-адреса, яка передається функції як
аргумент, записана у форматі "aaaa.bbbb.cccc". Це буде зроблено в завданні
11-го розділу.

Приклад роботи функції:

In [4]: convert_mac("1a1b.2c2d.3e3f")
Out[4]: '1a:1b:2c:2d:3e:3f'

In [5]: convert_mac("1111.2222.3333")
Out[5]: '11:11:22:22:33:33'

In [6]: mac_list = ["1a1b.2c2d.3e3f", "aaaa.bbbb.cccc", "1111.2222.3333"]

In [7]: for m in mac_list:
   ...:     print(convert_mac(m))
   ...:
1a:1b:2c:2d:3e:3f
aa:aa:bb:bb:cc:cc
11:11:22:22:33:33

У завданнях 9го розділу і далі, крім зазначеної функції, можна створювати
будь-які додаткові функції.
"""

mac_list = ["1a1b.2c2d.3e3f", "aaaa.bbbb.cccc", "1111.2222.3333"]

def convert_mac(data):
    res = data.split('.')
    res = [(x[:2], x[2:]) for x in res]
    res = ':'.join(':'.join(x) for x in res)
    return res


for m in mac_list:
    print(convert_mac(m))
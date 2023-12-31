# -*- coding: utf-8 -*-
"""
Завдання 6.6b

Зробити копію скрипта завдання 6.6a.
Доповнити скрипт: якщо адреса була введена неправильно, запитати адресу знову.

Якщо адреса неправильна, виводьте повідомлення: 'Wrong IP address'.
Повідомлення "Wrong IP address" має виводитися лише один раз після кожного
введення адреси, навіть якщо кілька пунктів перевірки адреси не виконано
(приклад виведення нижче).

Приклад виконання скрипту:
$ python task_6_6b.py
Enter IP address: 10.1.1.1
unicast

$ python task_6_6b.py
Enter IP address: a.a.a
Wrong IP address
Enter IP address: 10.1.1.1.1
Wrong IP address
Enter IP address: 500.1.1.1
Wrong IP address
Enter IP address: a.1.1.1
Wrong IP address
Enter IP address: 50.1.1.1
unicast

$ python task_6_6b.py
Enter IP address: 10.a.1.1.1
Wrong IP address
Enter IP address: 255.255.255.255
local broadcast

"""
from string import digits

res = 'Wrong IP address'
while res == 'Wrong IP address':
    ip = input('Enter IP address: ')
    flag = True
    if len((ip.split('.'))) != 4:
        flag = False
    elif not all(map(lambda x: x in digits, ''.join(ip.split('.')))):
        flag = False
    elif not all(map(lambda x: 0 <= int(x) <= 255, ip.split('.'))):
        flag = False

    if flag == True:

        if ip == '0.0.0.0':
            res = 'unassigned'
        elif ip == '255.255.255.255':
            res = 'local broadcast'
        elif 1 <= int(ip.split('.')[0]) <= 223:
            res = 'unicast'
        elif 224 <= int(ip.split('.')[0]) <= 239:
            res = 'multicast'
        else:
            res = 'unused'
    else:
        res = 'Wrong IP address'
    print(res)
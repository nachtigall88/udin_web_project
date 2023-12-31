# -*- coding: utf-8 -*-
"""
Завдання 6.6a

Зробити копію скрипта завдання 6.6.

Додати перевірку введеної IP-адреси.
Адреса вважається коректно заданою, якщо вона:
- складається з 4 чисел (а не літер чи інших символів)
- числа розділені точкою
- кожне число в діапазоні від 0 до 255

Якщо адреса неправильна, виводьте повідомлення: "Wrong IP address".  Якщо
адреса правильна, перевіряти та виводити тип адреси як у завданні 6.6.

Повідомлення "Wrong IP address" має виводитися лише один раз, навіть якщо
кілька пунктів вище не виконано.


Приклад виконання скрипту:
$ python task_6_6a.py
Enter IP address: 10.10.1.1
unicast

$ python task_6_6a.py
Enter IP address: 10.1.1
Wrong IP address

$ python task_6_6a.py
Enter IP address: a.a.10.1
Wrong IP address

$ python task_6_6a.py
Enter IP address: 50.1.a.a
Wrong IP address

$ python task_6_6a.py
Enter IP address: 10,1,1,1
Wrong IP address

$ python task_6_6a.py
Enter IP address: 500.1.1.1
Wrong IP address

$ python task_6_6a.py
Enter IP address: 50.1.1.1.1
Wrong IP address
"""
from string import digits

ip = input('Enter IP address: ')
flag = True
if len((ip.split('.'))) != 4:
    flag = False
elif not all(map(lambda x: x in digits, ''.join(ip.split('.')))):
    flag = False
elif not all(map(lambda x: 0 <= int(x) <= 255, ip.split('.'))):
    flag = False

if flag == True:
    res = ''
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
    print(res)
else:
    print('Wrong IP address')

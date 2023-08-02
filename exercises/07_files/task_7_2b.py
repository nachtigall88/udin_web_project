# -*- coding: utf-8 -*-
import sys
from sys import argv
"""
Завдання 7.2b

Скопіювати код із завдання 7.2a та переробити його: замість виведення на стандартний потік виведення, скрипт повинен записати отримані рядки у файл.

Імена файлів потрібно передавати як аргументи скрипту:
1 аргумент ім'я вихідного конфігураційного файлу
2 аргумент ім'я підсумкового файлу конфігурації, в який будуть записані рядки

Приклад роботи завдання:
$ task_7_2b config_sw1.txt new_config.txt

При цьому повинні бути відфільтровані рядки зі словами, які містяться в списку
ignore та рядки, що починаються на '!'.
"""

ignore = ["duplex", "alias", "configuration", "end", "service"]


if len(sys.argv) == 2:
    src_file = sys.argv[1]
    dest_filename = sys.argv[2]
else:
    src_file = 'config_sw1.txt'
    dest_filename = 'new_config.txt'

with open(src_file) as read_info, open(dest_filename, 'w') as written_info:
    for i in read_info:
        if '!' not in i and all(map(lambda x: x not in i, ignore)):
            written_info.write(i)

# print(sys.argv)
# C:/Users/Max/PycharmProjects/udin_web_project/exercises/07_files/task_7_2b.py
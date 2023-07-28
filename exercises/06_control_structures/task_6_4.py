# -*- coding: utf-8 -*-
"""
Завдання 6.4

Список файлів містить імена файлів:
["cfg_1.txt", "cfg_4.txt", "cfg_8.txt", "cfg_9.txt", "cfg_12.txt", "cfg_15.txt"]

Треба перейменувати файли таким чином:
["cfg_01.txt", "cfg_04.txt", "cfg_08.txt", "cfg_09.txt", "cfg_12.txt", "cfg_15.txt"]

Тобто треба зробити так, щоб після cfg_ завжди було дві цифри. Якщо число менше
10, доповнити до 2 цифр нулями на початку.

Написати код, який перетворює імена файлів у потрібний формат і додає їх до
нового списку result (тест перевірятиме змінну result). Отриманий список
результату вивести на стандартний потік виведення (stdout) за допомогою print.

Вихідний список files не можна змінювати вручну, всі зміни треба зробити за
допомогою Python. Також бажано не прив'язуватись до положення файлу у списку.
"""

files = [
    "cfg_1.txt", "cfg_4.txt", "cfg_8.txt", "cfg_9.txt", "cfg_12.txt", "cfg_15.txt"
]
mid = [x.split('.') for x in files]
mid2 = [x[0].split('_') for x in mid]
mid3 = [y[-1].rjust(2, '0') for y in mid2]
res = list(map(lambda x, y: x[0] + '_' + y, mid2, mid3))
result = list(map(lambda x, y: x+'.'+y[-1], res, mid))
# print(mid)
# print(mid2)
# print(mid3)
# print(res)
print(result)

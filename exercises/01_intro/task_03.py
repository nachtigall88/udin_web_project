"""
Якщо запустити код завдання, на екран буде виведено:
$ python task_03.py
Python is a high-level, interpreted, general-purpose programming language.

Отримати з рядка start_data такий список (видалені коми та точка і рядок
поділено на слова):
['Python', 'is', 'a', 'high-level', 'interpreted', 'general-purpose', 'programming', 'language']

За допомогою print вивести отриманий список на екран:
$ python task_03.py
['Python', 'is', 'a', 'high-level', 'interpreted', 'general-purpose', 'programming', 'language']

Тут дуже важливий момент, що треба отримати саме список (тип даних), а не,
наприклад, рядок, який схожий на зображений список.

Обмеження: рядок start_data не можна змінювати вручну, тільки за допомогою Python.
"""
start_data = "Python is a high-level, interpreted, general-purpose programming language."
start_data = [x.rstrip(',') for x in start_data[:-1].split()]
print(start_data)
# print(start_data == ['Python', 'is', 'a', 'high-level', 'interpreted', 'general-purpose', 'programming', 'language'])


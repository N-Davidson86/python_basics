"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

print('task_3\n')
n = input("Введите число для подсчета: ")
nn = int(n + n)
nnn = int(n + n + n)
n = int(n)
result = n + nn + nnn
print(result)

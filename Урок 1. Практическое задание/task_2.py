"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
print('task_2\n')
sec = int(input("Введите время в секундах: "))
res = datetime.timedelta(seconds=sec)
print(res)
print('\nlook at another variant\n')
sec = int(input('Введите кол-во секунд для преобразования в чч:мм:сс '))
seconds = sec % (24 * 3600)
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(f'{hour}:{minutes}:{seconds}\n\n')


"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

month = int(input("Enter number of month (1-12): "))

month_list = ["winter", "winter", "spring", "spring", "spring", "summer",
              "summer", "summer", "autumn", "autumn", "autumn", "winter"]

print(f'Вывод из списка: {month_list[month -1]}')

month_dict = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring",
              6: "summer", 7: "summer", 8: "summer", 9: "autumn",
              10: "autumn", 11: "autumn", 12: "winter"}
print(f'Вывод из словаря: {month_dict.get(month)}')

print("Методы разные - результат один!")


# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: 6782 -> 23        0,56 -> 11

number = float(input('Введите число:'))
sum = 0
for i in str(number):
    if i != ".":
        sum += int(i)
print(f'Сумма цифр = {sum}')
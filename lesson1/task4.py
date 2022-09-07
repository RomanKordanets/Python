# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти 1-4:'))

if quarter == 1:
    print('X(0,+Infinity), Y(0,+Infinity)')
elif quarter == 2:
    print('X(0,-Infinity), Y(0,+Infinity)')
elif quarter == 3:
    print('X(0,-Infinity), Y(0,-Infinity)')
elif quarter == 4:
    print('X(0,+Infinity), Y(0,-Infinity)')
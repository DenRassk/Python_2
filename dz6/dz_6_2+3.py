# Условие 2 задачи
# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите,
# есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Условие 3 задачи:
# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

# тут реализуем запускающий модуль для двух задач с ферзями

from dz_6_2_3.dz_6_2_gen_queen import gen_queen
from dz_6_2_3.dz_6_2_check_queen import check_queen

_NEED_OK_POSITIONS = 4  # Требуемое кол-во успешных расстановок
total_position = 0      # общее количество сгенерированых расстановок
count_ok = 0            # подсчёт удачных расстановок
list_ok_positions = []  # список удачных расстановок

print(f"Идёт генерация и проверка {_NEED_OK_POSITIONS} расстановок ферзей...")
while count_ok < _NEED_OK_POSITIONS:
    generated_position = gen_queen()
    total_position += 1
    if check_queen(generated_position):
        list_ok_positions.append(generated_position)
        count_ok += 1

print(f" Всего сгенерировано {total_position}, удачные:")
for pos in list_ok_positions:
    print(pos)
# Напишите однострочный генератор словаря,
# который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и
# суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

# сумма форматируется для отображения 2 знаков после запятой

name = ['Пётр', 'Василий', 'Сергей', 'Максим']
bet = [1000, 2000.2, 3000, 4000.4]
prize = ['10.25%', '5.12%', '3.41%', '2.56%']

dict = {}
for i in range(len(name)):
    dict[name[i]] = format(float(prize[i][:-1]) * float(bet[i]), '.2f')

dict_new = {n: format((float(p[:-1]) * float(b)), '.2f') for n, b, p in zip(name, bet, prize)}

print(f'Словарь по "старому": {dict}')
print(f'Словарь по "новому" : {dict_new}')
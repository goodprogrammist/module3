# Цель задания
# Научиться работать с базовым синтаксисом Python.
def input_number(text):
    try:
        num = int(input(text))
        print("Ввод корректен")
        return num
    except ValueError:
        print("Вы точно вводите число? Попробуйте снова.")
        input_number(text)


# Что нужно сделать:
# Зайдите в файлы с заданиями и выполните так чтобы вывод соотвествовал условиям.
print('Задача 1. Язык математики')
print()
# Маше для защиты курсовой работы нужно написать программу для расчёта экономической модели по формуле.
# Как записать саму формулу в программу, она не знает, у неё есть только начальные значения.
# Поэтому Маша решила просто заплатить Егору, чтобы тот написал её быстрее.
#
# Дана программа:
# a = 8
# b = 10
# c = 12
# d = 18
#
# Продолжите программу:
# переведите выражение с математического языка на язык Python, запишите его в переменную res и выведите результат.
#
# Выражение:

# (-3 + a**2) * b - 2**3
#      c- 2 * d

a = 8
b = 10
c = 12
d = 18

res = ((a**2 - 3) * b - 2**3) / (c - 2 * d)
print('Результат рассчёта:', res)

print()
print()
print('Задача 2. Финансовый отчёт')
print()
# Наде дали задание сформировать финансовый отчёт за последние 20 лет по полугодиям.
# Нужно сумму дохода первых двух кварталов поделить на сумму последних двух кварталов,
# чтобы понять динамику роста или падения дохода. И так за каждый год.
#
# Надя решила,
# что быстрее будет написать простую программу, которая сделает всё за неё.
#
#
# Запросите у пользователя четыре числа.
# Отдельно сложите первые два и отдельно вторые два.
# Разделите первую сумму на вторую.
# Выведите результат на экран.

# текущий год всегда неполный так как финансовые данные будут с опозданием на месяц-три.
year = 2021
while year > 2000:
    year -= 1  # Уходим в прошлые годы
    text = ' Введите доход первого квартала ' + str(year) + ' года: '
    quarter_1 = input_number(text)
    print('Принято число', quarter_1)
    text = ' Введите доход второго квартала ' + str(year) + ' года: '
    quarter_2 = input_number(text)
    print('Принято число', quarter_2)
    text = ' Введите доход третьего квартала ' + str(year) + ' года: '
    quarter_3 = input_number(text)
    print('Принято число', quarter_3)
    text = ' Введите доход четвертого квартала ' + str(year) + ' года: '
    quarter_4 = input_number(text)
    print('Принято число', quarter_4)
    # тут получены полные данные за год. Начинаю считать
    trend = (quarter_1 + quarter_2) / (quarter_3 + quarter_4)
    print('Динамика за ' + str(year) + ' год: ' + str(trend))

# Цель задания
# Научиться работать с базовым синтаксисом Python.
def input_number(text):
    try:
        num = int(input(text))
        #print("Ввод корректен")
        return num
    except ValueError:
        print("Вы точно вводите число? Попробуйте снова.")
        return input_number(text)


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
while year > 2000:  # чтобы быстрее проверить - поставить тут 2020
    year -= 1  # Уходим в прошлые годы
    text = 'Введите доход первого квартала ' + str(year) + ' года: '
    quarter_1 = input_number(text)
    #print('Принято число', quarter_1)
    text = 'Введите доход второго квартала ' + str(year) + ' года: '
    quarter_2 = input_number(text)
    #print('Принято число', quarter_2)
    text = 'Введите доход третьего квартала ' + str(year) + ' года: '
    quarter_3 = input_number(text)
    #print('Принято число', quarter_3)
    text = 'Введите доход четвертого квартала ' + str(year) + ' года: '
    quarter_4 = input_number(text)
    #print('Принято число', quarter_4)
    # тут получены полные данные за год. Начинаю считать
    trend = (quarter_1 + quarter_2) / (quarter_3 + quarter_4)
    print()
    print('Динамика за ' + str(year) + ' год: ' + str(trend))

print()
print()
print('Задача 3. Следующее и предыдущее')
print()

# В олимпиаде по программированию участвовали 1000 человек,
# и программа автоматически распределила их по количеству баллов.
# Иногда количество баллов у участников одинаковое,
# и тогда комиссии нужно посмотреть фамилии одного из таких участников,
# а также его соседей, это реализует специальная часть алгоритма.
#
# Напишите программу,
# которая получает от пользователя число и выводит на экран два ответа — следующее и предыдущее число.
# Результат:

# Введите число: 5
# После числа 5 идет число 6
# До числа 5 идет число 4

number = input_number('Введите число: ')
print('После числа', number, 'идёт число', number + 1)
print('До числа', number, 'идёт число', number - 1)

print()
print()
print('Задача 4. Площадь треугольника')
print()
# Напишите программу,
# которая запрашивает у пользователя длины двух катетов
# в прямоугольном треугольнике и выводит его площадь.

# Формула:
# S = ab/2

katet1 = input_number('Введите длину первого катета: ')
katet2 = input_number('Введите длину второго катета: ')

square = katet1 * katet2 / 2
print('Площадь = ', square)

print()
print()
print('Задача 5. Часы')
print()
# Напишите программу,
# которая получает на вход число n — количество минут, — затем считает,
# сколько это будет в часах и сколько минут останется,
# и выводит на экран эти два результата.

min = input_number('Сколько минут? ')
hours = min // 60
rest = min % 60
print('Это', hours, 'ч.', rest, 'мин.')

print()
print()
print('Задача 6')
print()
# Реализуйте программу,
# которая запрашивает два числа у пользователя.
# После этого у каждого числа возьмите две последние цифры.
# Получившиеся два числа сложите и выведите на экран.

# Пример:
# Введите первое число: 456
# Введите второе число: 123
# Сумма: 79

number_1 = input_number('Введите первое число: ')
number_2 = input_number('Введите второе число: ')

ost1 = number_1 % 100
ost2 = number_2 % 100

print("Сумма:", ost1 + ost2)

print()
print()
print('Задача 7. Поездка по кругу')
print()
# Вася решил потренироваться перед марафоном и покататься вокруг Москвы на скорость.
# Длина дороги — 115 километров.
# Вася стартует с нулевого километра и едет со скоростью v километров в час.
# На какой отметке он остановится через t часов?
#
# Реализуйте программу,
# которая спрашивает у пользователя v и t,
# и выводит целое число от 0 до 114 — номер километра, на котором остановится Вася.
# Учтите, что он может прокатиться больше одного круга.

v = input_number('Введите скорость Васи (км/ч): ')
t = input_number('Введите время (ч): ')

path = v * t

km = path % 115

print('Вася на', km, 'километре')

print()
print()
print('Задача 8. Режем число на части')
print()
# Реализуйте программу,
# которая получает на вход четырёхзначное число
# и выводит на экран каждую его цифру отдельно
# (в одну строчку либо каждая цифра в новой строчке).
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных

number = input_number('Введите четырёхзначное число для разрезания: ')

r1 = number // 1000
r2 = (number - r1 * 1000) // 100
r3 = (number - r1 * 1000 - r2 * 100) // 10
r4 = number % 10

print(r1, r2, r3, r4)

print()
print()
print('Задача 9. В обратном порядке')
print()
# Реализуйте программу,
# которая получает на вход четырёхзначное число и выводит его на экран в обратном порядке.
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных.
# Пример ввода: 1234.
# Пример вывода: 4321.

number = input_number('Введите четырёхзначное число для его переворачивания: ')

r1 = number // 1000
r2 = (number - r1 * 1000) // 100
r3 = (number - r1 * 1000 - r2 * 100) // 10
r4 = number % 10

res = r4 * 1000 + r3 * 100 + r2 * 10 + r1

print(res)

print()
print()
print(
    'Задача 10. Поменять местами: не всё так просто! (необязательная, повышенной сложности)'
)
print()
# Мы умеем менять местами строковые переменные и знаем,
# что в переменных, кроме строк, можно хранить и числа.
# Напишите программу, которая меняла бы значения двух переменных местами,
# но без использования третьей переменной и без использования  синтаксического сахара,
# который мы разбирали, а именно — без конструкции a,b = b,a.
# В переменные будут вводиться только числа.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
# стереть эту строчку и вставить свой код здесь
a = a + b
b = a - b
a = a - b
print(a, b)

# Изменять, удалять, менять местами 10-ю, 11-ю, 12-ю и 14-ю строчки нельзя.
# Но в 13-ю строку можно вставлять сколько угодно кода, не трогая последний принт.

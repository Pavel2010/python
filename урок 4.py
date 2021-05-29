# задание 1

from sys import argv

файл, выработка, ставка, премия = argv
расчет = (int(выработка) * int(ставка)) + int(премия)
print(f'зарплата равна {расчет}')

задание 2

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list = [el for el in my_list if el > my_list[my_list.index(el) - 1]]
print(list)

задание 3

num = range(20, 241)
list = [el for el in num if el % 20 == 0 or el % 21 == 0]
print(list)

задание 4

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list = [el for el in my_list if my_list.count(el) == 1]
print(list)

задание 5

from functools import reduce
my_list = [el for el in range(100, 1001) if el % 2 == 0]
def my_func(el1, el2):
    return el1 * el2

print(reduce(my_func, my_list))

задание 6

from itertools import count
from itertools import cycle

def count_func(первое_число, последнее_число):
    for el in count(первое_число):
        if el > последнее_число:
            break
        else:
            print(el)
def cycle_func(список, итерация):
    i = 0
    итер = cycle(список)
    while i < итерация:
        print(next(итер))
        i+=1
count_func(первое_число = int(input("введите первое число: ")), последнее_число = int(input("введите последнее число: ")))
cycle_func(список=['а', 'б'], итерация=int(input("введите итерацию: ")))
















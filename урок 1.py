# задание 1
name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
age = int(input("Введите свой возраст: "))
print(f'Имя {name}, Фамилия {surname}, Возраст {age}')

# задание 2

a = int(input("Введите время в секундах: "))
h = a // 3600
m = (a // 60) % h
s = a % 60
print(f"{h}:{m}:{s}")

# задание 3

n = int(input("Введите число: "))
s = str(n)
s1 = s + s
s2 = s + s + s
n = n + int(s1) + int(s2)
print(n)

# задание 4

num = int(input("Введите целое положительное число: "))
m = num % 10
while num > 0:
    if num % 10 > m:
         m = num % 10
    num = num // 10
    print(m)

# задание 5

p = int(input("Введите выручку: "))
c = int(input("Введите издержки: "))
if (p - c) > 0:
    print("Выручка больше издержек")
    print("Прибыль =", (p - c))
    s = int(input("Введите колличество сотрудников: "))
    print("Прибыль на одного сотрудника =", (p - c) / s)
elif (p - c) < 0:
    print("Издержки больше выручки")



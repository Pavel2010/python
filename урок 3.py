# задание 1

def my_func (a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return "b не должно = 0"
print(my_func(int(input("Введите число а: ")), int(input("Введите число b: "))))

# задание 2

def my_func(Имя, Фамилия, год_рождения, город_проживания, email, телефон):
        print(Имя, Фамилия, год_рождения, город_проживания, email, телефон)

my_func(Имя='Павел', Фамилия='Федоров', год_рождения='1981', город_проживания='Москва',
        email='pavelfd@yandex.ru', телефон='+79265309937')

# задание 3

def my_func(a, b, c):
        li = [a, b, c]
        summa = []
        max_1 = max(li)
        summa.append(max_1)
        li.remove(max_1)
        max_2 = max(li)
        summa.append(max_2)
        print(sum(summa))
my_func(3, 5, 9)

# задание 4

def my_func(x, y):
    return 1 / x ** abs(y)
print(my_func(5, -2))

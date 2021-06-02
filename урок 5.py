# Задание 1

my_list = []
while True:
    line = input("Введите текстовую строку: ")
    if line == '':
        print(my_list)
        exit()
    else:
        newline = line + '\n'
        my_list.append(newline)

    with open("text_1.txt", "w", encoding='utf-8') as file:
        file.writelines(my_list)

# Задание 2

my_list = ['Всем привет\n', 'Досвидания\n', 'Всего хорошего\n']
with open("text_1.txt", 'w+', encoding='utf-8') as file:
    file.writelines(my_list)
with open("text_1.txt") as file:
    lines = 0
    letters = 0
    for line in file:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"Колличество букв в строке{letters}")
    print(f"Колличество строк {lines}")

# задание 3

company = {'Федоров': 30000, 'Иванов': 21000, 'Сидоров': 19000, 'Петров': 17000}
try:
    file = open("text_1.txt", 'w', encoding='utf-8')
    for Фамилия, Зарплата in company.items():
        file.write(Фамилия + ':' + str(Зарплата) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file.close()
summa = 0
count = 0
persons = []
with open("text_1.txt", "r", encoding='utf-8') as file:
    for line in file:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 20000:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"Сотрудники: {persons}")
print(f"Средний доход: {result}")




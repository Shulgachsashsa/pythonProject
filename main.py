import ast
from ast import literal_eval


def main():
    while True:
        print("Выбор заданий: ")
        print("1. Задание 1")
        print("2. Задание 2")
        print("3. Задание 3")
        print("4. Задание 4")
        print("5. Завершение программы")
        value = input("Выберете пункт меню: ")

        try:
            value = int(value)
        except Exception:
            print("Некорректный ввод! Попробуйте заново!")
            continue

        match value:
            case 1:
                n = input("Введите целое число: ")
                try:
                    n = int(n)
                    result = FirstTask(n)
                    print(result)
                except ValueError:
                    print("Некорректный ввод")
            case 2:
                inp = input("Введите строку, число, список или кортеж: ")
                try:
                    value = ast.literal_eval(inp)
                    SecondTask(value)
                except Exception as e:
                    print("Ошибка. Ввод не обработан.")
            case 3:
                ThirdTask()
            case 4:
                FourthTask()
            case 5:
                print("Пока!")
                break
            case _:
                return ("Некорректный ввод данных! Попробуйте заново!")

def FirstTask(n):
    a = 0
    b = 1
    sum = 0
    while a < n:
        sum += a
        temp = a
        a = b
        b = temp + b
    return sum


def SecondTask(value):
    if isinstance(value, tuple):
        print("Введенные данные являются кортежем!")
        for word in value:
            if isinstance(word, str):
                length = len(word)
                print(f"Длина слова '{word}' составляет {length} символов")
            else:
                print(f"'{word}' не является строкой.")

    elif isinstance(value, list):
        print("Введенные данные являются списком!")
        letter_count = 0
        number_count = 0
        for item in value:
            if isinstance(item, str):
                for char in item:
                    if char.isalpha():
                        letter_count += 1
            elif isinstance(item, (int, float)):
                number_count += 1

        print(f"Количество букв в списке: {letter_count}")
        print(f"Количество чисел в списке: {number_count}")

    elif isinstance(value, (int, float)):
        print("Введенные данные являются числом!")
        sum = 0
        while value != 0:
            temp = value % 10
            if temp % 2 != 0:
                sum += temp
            value //= 10
        print(f"Сумма нечетных цифр введенного числа равна {sum}")

    elif isinstance(value, str):
        print("Введенные данные являются строкой!")
        letter_count = 0
        for char in value:
            if char.isalpha():
                letter_count += 1
        print(f"Количество букв в введенной строке '{value}' = {letter_count}")
    else:
        print("Введенные данные не соответствуют ни одному из ожидаемых типов.")

def ThirdTask():
    rows = int(input("Введите количество строк: "))
    columns = int(input("Введите количество столбцов: "))
    matrix = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = int(input(f"Введите элемент матрицы {i+1} {j+1}: "))
    print("Введенная матрица: ")
    for i in matrix:
        print(i)
    temp = 0
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] < 0:
                temp += 1
                break
    if temp != rows:
        print("В матрице не в каждой строке присутствует отрицательный элемент!")
    else:
        for i in range(rows):
            for j in range(columns):
                matrix[i][j] = matrix[i][j] * -1
        print("Итоговая матрица: ")
        for i in matrix:
            print(i)

def FourthTask():
    try:
        while True:
            mood = input("Какое у вас сейчас настроение: :) - хорошее; :( - грустное? ")
            if mood == ":(" or mood == ":)":
                break
            else:
                print("Некорректный ввод! Попробуйте заново!")
        if mood == ":)":
            print("У вас хорошее настроение!")
        elif mood == ":(":
            raise ValueError("Грустное настроение")
    except ValueError as e:
        print(
            f"Перехвачена ошибка ввиде вашего плохого настроения. Вот шутка для вас: Почему птицы не используют Facebook? Потому что у них уже есть Twitter! :)")
    finally:
        print("Желаю вам хорошего дня!")

main()
#Практическая 7, 1 вариант, задание 1
def x():
    n = int(input("Введите размер массива: "))
    array = []

    for i in range(n):
        element = int(input("Введите элемент массива: "))
        array.append(element)

    z = max(array)
    print("Максимальный элемент:", z)

    y = array[::-1]
    print("Массив в обратном порядке:", y)

x()
#Задание 2
def x():
    n = int(input("Введите размер массива: "))
    array = []

    for i in range(n):
        element = float(input("Введите элемент массива: "))
        array.append(element)

    average = sum(array) / len(array)

    for i in range(len(array)):
        if array[i] == 0:
            array[i] = average

    print("Массив с замененными нулевыми элементами:", array)

x()
#задание 1
def x(n):
    i = 1
    while i**2 <= n:
        print(i**2)
        i += 1
n = int(input("Введите целое число N: "))
x(n)
#задание 2
def y(n):
    i = 2
    while i <= n:
        if n % i == 0:
            return i
        i += 1
n = int(input("Введите целое число N: "))
y = y(n)
print("Наименьший натуральный делитель числа", n, ":", y)
#задание 3 
def x(n):
    y = 0
    z = 1
    while z * 2 <= n:
        z *= 2
        y += 1
    return y, z
n = int(input("Введите натуральное число N: "))
y, z = x(n)
print("Наибольшая целая степень двойки, не превосходящая", n, ":", y)
print("Сама степень:", z)
#задание 4
def z(x, y):
    distance = x
    day = 1
    while distance < y:
        distance += distance * 0.1
        day += 1
    return day
x = float(input("Введите начальный пробег спортсмена: "))
y = float(input("Введите желаемый пробег спортсмена: "))
day = z(x, y)
print("На", day, "день пробег спортсмена составит не менее", y, "километров.")
#задание 5
x = 0
while True:
    num = int(input("Введите число: "))
    if num == 0:
        break
    x += 1

print("Количество членов последовательности:", x)
#задание 6
x = 0
y = 0
while True:
    z = int(input("Введите число: "))
    if z == 0:
        break
    x += z
    y += 1

if y > 0:
    average = x / y
else:
    average = 0

print("Среднее значение всех элементов последовательности:", average)
#задание 7
x = 0
prev = float(input("Введите первое число: "))
while True:
    num = float(input("Введите следующее число: "))
    if num == 0:
        break
    if num > prev:
        x += 1
    prev = num

print("Количество элементов последовательности, больших предыдущего элемента:", x)
#задание 8
x = 0
y = 1
prev = int(input("Введите первое число: "))
while True:
    num = int(input("Введите следующее число: "))
    if num == 0:
        break
    if num == prev:
        y += 1
    else:
        if y > x:
            x = y
        y = 1
    prev = num

print("Наибольшее число подряд идущих элементов, равных друг другу:", x)



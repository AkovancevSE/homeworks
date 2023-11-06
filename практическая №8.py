#Практическая 8, вариант 1, задание 1
import math

def square():
    side = float(input("Введите длину стороны квадрата: "))
    area = side ** 2
    print("Площадь квадрата:", area)

def rectangle():
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))
    area = length * width
    print("Площадь прямоугольника:", area)

def circle():
    radius = float(input("Введите радиус окружности: "))
    area = math.pi * radius ** 2
    print("Площадь окружности:", area)

def triangle():
    base = float(input("Введите длину основания треугольника: "))
    height = float(input("Введите высоту треугольника: "))
    area = 0.5 * base * height
    print("Площадь треугольника:", area)

square()
rectangle()
circle()
triangle()

#Задание 2
def all(array):
    sum_of_elements = sum(array)
    average_value = sum_of_elements / len(array)
    return sum_of_elements, average_value
array1 = [1, 2, 3, 4, 5]
array2 = [10, 20, 30]
array3 = [100, 200, 300, 400]
sum1, average1 = all(array1)
sum2, average2 = all(array2)
sum3, average3 = all(array3)
print("Сумма элементов в первом массиве:", sum1)
print("Среднее арифметическое значение в первом массиве:", average1)

print("Сумма элементов во втором массиве:", sum2)
print("Среднее арифметическое значение во втором массиве:", average2)

print("Сумма элементов в третьем массиве:", sum3)
print("Среднее арифметическое значение в третьем массиве:", average3)
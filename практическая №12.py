# задание 1
def calculateFactorial(number: int) -> int:
    if number == 0:
        return 1
    return calculateFactorial(number - 1) * number

def calculateExpression(x: int, n: int) -> float:
    return x ** n / calculateFactorial(n)

value: int = calculateExpression(3, 5)
print(value)
# задание 2
def getSecondMax(array: list) -> int:
    if array[-1] != 0:
        array.append(0)
    array.remove(max(array))
    return max(array)

numbers = [1, 5, 7, 8, 23, 67, 12, -1, 0]
secondMax = getSecondMax(numbers)
print(secondMax)
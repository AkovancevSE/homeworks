print("№1")
print("Курс Основы программирования начался")
print("   ")

print("№2")
print((16823*12302)%3092)
print("   ")

print("№3")
age = 17
if age>=16:
    print("Поздравляем, Вы поступили в ВГУИТ")
else:
    print("сначала нужно окончить школу")
if 0< age < 75:
    print(True)
else:
    print(False)
name = "Илья"
if name != "Иван":
    print(True)
else:
    print(False)
if age < 16:
    print("осталось учиться", 16 - age, "лет")
print("   ")

print("№4")
secounds = 1000008
days = secounds // 86400
hours = (secounds % 86400) // 3600
minutes = (secounds % 3600) // 60
seconds = secounds % 60
print( "дни:", days, ";", "часы:", hours,";", "минуты:", minutes,";", "секунды:", seconds)

print("   ")

print("№5")
n = 2
print(n + n**2 + n**3 + n**4 + n**5)

print("   ")

print("№6")
x = 9
y = 8
print(x, y)
x, y = y, x
print(x, y)

print("   ")

print("№7")
number = 17
if number%2 == 0:
    print(True)
else:
    print(False)

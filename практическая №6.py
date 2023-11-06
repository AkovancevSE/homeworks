#Практическая 6, 1 вариант
def x(string):
    words = string.split()
    count = 0
    for word in words:
        if word.startswith('е') or word.startswith('Е'):
            count += 1
    return count

string = "Еще бы сегодня ее не было тут."
print(x(string))
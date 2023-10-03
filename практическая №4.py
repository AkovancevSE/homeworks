print("№1")
B = 110
while A<=B:
    print(A)
    A+=1
print("   ")

print("№2")
A = int(input())
B = int(input())
if A <= B:
    while A<=B:
        print(A)
        A+=1
else:
    while A >= B:
        print(A)
        A-=1
print("  ")

print("№3")
A = 10
B = 21
while A <= B:
    if A %2 !=0:
        print(A)
        A+=1
    else:
        A += 1
print("  ")

print("№4")
n = int(input())
sum = 0
for i in range(n):
    sum += int(input())
print(sum)
print("  ")

print("№5")
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i ** 3
print(sum)
print("  ")

print("№6")
res = 1
n = int(input())
for i in range(1, n + 1):
    res *= i
print(res)
print("  ")

print("№7")
n = int(input())
res = 1
sum = 0
for i in range(1, n + 1):
    res *= i
    sum += res
print(sum)
print("  ")

print("№8")
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()
print("  ")

print("№9")
def task(n):
    s, c, p = 0, 0, 1
    for _ in range(n):
        c, p = c + p, c
        s += c
    return s
n = int(input("n="))
print(task(n))
print("  ")

print("№10")
lst = [0, 1]
n, k = int(input('введите число: ')), int(input('введите число: ')) - 1
for i in range(1, n + 1):
    lst.append(lst[-2] + lst[-1])
print(sum(lst[k: len(lst)]))


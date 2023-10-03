print("№1")
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
print("   ")

print("№2")
a = int(input())
b = int(input())
S = 0.5 * a * b
print(S)
print("  ")

print("№3")
n = int(input())
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)
print("   ")

print("№4")
a = int(input())
b = int(input())
l = int(input())
N = int(input())
print((l*2)+(2*(b*(N-1)))+(2*(a*N)-a))
print("  ")

print("№5")
def Minn(a, b, c):
    if a<b and a <c:
        return a
    elif b < c and b < a:
        return b
    elif c < a and c < b:
        return c
a = int(input())
b = int(input())
c = int(input())
print("минимальное",Minn(a, b, c))
print("  ")

print("№6")
def N(a, b, c, d):
    if (a + b + c + d)%2 == 0:
        return "Да"
    else:
        return "Нет"
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(N(a, b, c, d))
print("  ")

print("№7")
def Year(n):
    if n%4 == 0 and n%100 != 0 or n%400 == 0:
        return ("Yes")
    else:
        return("No")
n = int(input())
print(Year(n))
print("  ")

print("№8")
def S(a, b, c):
    if a == b == c:
        return "3"
    elif a == b and a != c:
        return "2"
    elif b == c and b!= a:
        return "2"
    elif a== c and a != b:
        return "2"
    elif a != c and a!= b and c != b:
        return "0"
a = int(input())
b = int(input())
c = int(input())
print(S(a, b, c))
print("  ")


print("№9")
def SH(n, m, k):
    if k < m * n and (k % m == 0 or k % n == 0):
        return('YES')
    else:
        return('NO')
n = int(input())
m = int(input())
k = int(input())
print(SH(n, m, k))




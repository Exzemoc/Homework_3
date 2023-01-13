x = int(input('Число: '))
y = sum(i ** 3 for i in range(1, x + 1))
print(y)

n = int(input('Число: '))
c = 0
while 1 <= n:
    n -= 1
    b = (n + 1) ** 3
    c += b
print(c)

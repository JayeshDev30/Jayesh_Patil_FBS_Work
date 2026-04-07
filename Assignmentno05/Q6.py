n = 10
i = 2

while n > 0:
    if all(i % d for d in range(2, i)):
        print(i)
        n -= 1
    i += 1
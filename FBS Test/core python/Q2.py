num = int(input("Enter number: "))
sum = 0
fact = 1
for i in range(1, num + 1):
    fact *= i 
    temp = i / fact
    sum += temp

print('The sum of the series is:', sum)
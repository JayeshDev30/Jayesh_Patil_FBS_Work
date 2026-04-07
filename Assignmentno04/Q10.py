num = int(input("Enter the Number :"))
sum = 0
for i in range(1,num):
    if num % i == 0:
        sum += i
if sum == num:
    print(num, "is a perfect number.")
else:
    print(num, "is a not perfect number. ")             


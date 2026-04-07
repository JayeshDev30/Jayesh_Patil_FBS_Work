number = int(input("Enter a number: "))
num1 = str(number)
num2 = len(num1)

sum = 0
for digit in num1:
    sum += int(digit) ** num2

if sum == number:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
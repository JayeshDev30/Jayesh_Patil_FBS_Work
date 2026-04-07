lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print(f"Armstrong numbers between {lower} and {upper}:")

for num in range(lower, upper + 1):
    num1 = str(num)
    num2 = len(num1)
    
    total = sum(int(d) ** num2 for d in num1)
    
    if num == total:
        print(num)
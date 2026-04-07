num1 =int(input('Enter N1 :'))
num2 =int (input('Enter N2 :'))

print(f"Original values: num1 = {num1}, num2 = {num2}")

temp = num1
num1 = num2
num2 = temp

print(f"Swapped values: num1 = {num1}, num2 = {num2}")



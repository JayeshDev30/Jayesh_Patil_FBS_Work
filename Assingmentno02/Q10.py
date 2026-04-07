num = int(input('Enter 3 digit number :'))
temp = num

d1 = temp % 10
temp = temp // 10

d2 = temp % 10
temp = temp// 10

d3 =  temp % 10
temp //= 10

print(f'Reversed Number :{d1}{d2}{d3}')




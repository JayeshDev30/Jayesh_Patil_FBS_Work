num = int(input('Enter 3 digit :'))
if(100 <= num <= 999):
    hundreads = num // 100
    tens = num // 10
    unit = num % 10

    sum_of_digit = hundreads + tens + unit

    print('Sum of Digits :', sum_of_digit)
else:
    print('Enter a valid number ')

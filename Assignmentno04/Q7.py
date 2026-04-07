num = int(input('Enter the number :'))
i = 1
print("Number is not divisible by 2 and 3")
for i in range(i,num+1):
    if(i % 2 !=0 and i % 3!=0):
     print(i)
     i = i+1
     
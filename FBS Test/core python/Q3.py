num = int(input('Enter Basic salary : '))

DA = 0.10*num
TA = 0.12*num
HRA = 0.15*num

sum = num * (1 + 0.10 + 0.12 + 0.15)

print('DA : ',DA)
print('TA :',TA)
print('HRA : ',HRA)
print('TS :',sum)
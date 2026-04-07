gender = input('Enter gender (M/F) : ')
age = int(input('Enter the age : '))
if(gender == '[F,f,FEMALE,Female,female]'):
  if(age >=18):
     print('Eligible for Marriage')
  else:
     print('Phele Padhayi Kar loo')
else:    
  if(age >= 21):
     print('Eligible for Marriage')
  else:
     print('Pehle Kama loo')
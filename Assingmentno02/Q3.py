feet = float(input ('Enter a distance in feet : '))
inches = float( input ('Enter a distance in inches : '))

convertingfeet_into_inches = (feet * 12) + inches

convertinginches_into_meter = (convertingfeet_into_inches * 2.54) 
meter = convertinginches_into_meter / 100


print('Distance in meter :', meter)
print('Distance in centimeter :', convertingfeet_into_inches)
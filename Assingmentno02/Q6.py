basic = float(input ('Enter a Basic salary :'))

Dearness = 0.10*basic
Traveling_allownance = 0.12*basic
house_rate_allownance = 0.15*basic

total_salary = basic + Dearness + Traveling_allownance + house_rate_allownance

print('Basic Salary :', basic)
print('Dearness (10%) :', Dearness)
print('Traveling_allownance (12%) :', Traveling_allownance)
print('house_rate_allownance (15%) :',house_rate_allownance)
print('Total Salary :',total_salary )
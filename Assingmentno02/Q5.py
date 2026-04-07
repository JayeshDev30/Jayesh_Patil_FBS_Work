
cost_price = float(input("Enter cost price: "))
discount = float(input("Enter discount percentage: "))

selling_price = cost_price - (cost_price * discount / 100)
print("The selling price is:", selling_price)
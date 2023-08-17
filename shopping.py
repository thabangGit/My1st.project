#asking the user to enter the names of three products

product1_name = input("Enter name of the product 1:" )
product2_name = input("Enter name of the product 2:" )
product3_name = input("Enter name of the product 3:" )

#prices of three different product

product1_price = float(input(f"Enter the price of {product1_name}: "))
product2_price = float(input(f"Enter the price of {product1_name}: "))
product3_price = float(input(f"Enter the price of {product1_name}: "))

# Calculating the sum of all three product prices

total_price = product1_price + product2_price + product3_price

#average prices of three products

average_price = total_price / 3

# Rounding the total price and average price to two decimal places using the round() function

rounded_total_price = round(total_price, 2)
rounded_average_price = round(average_price, 2)

# Printing out the entered information and the rounded total price and average price

print("product and prices:")
print(f"{product1_name}: R{product1_price:.2f}")
print(f"{product2_name}: R{product2_price:.2f}")
print(f"{product3_name}: R{product3_price:.2f}")
print(f"The total of {product1_name}, {product2_name}, {product3_name}, is R{rounded_total_price:.2f} and the average price of the items is ${rounded_average_price:.2f}")


#the last code isnt mine , i got it online but i do understand how it works though 
#the code that isn't mine start from *print till print (f"the total)*
#The .2f part after the colon is used to format the number with two decimal places, which is common when dealing with money.
#The f before the string tells Python that you want to make a special sentence.
#The "R" symbol right before {product1_price:.2f} is just a way to show that the number following it represents a price in Rands.
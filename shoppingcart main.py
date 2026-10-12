

#  bug store product prices as integers (or floats)
headPhone = 999
smartWatch = 1599
PS5 = 1299
iPad = 599

productName = input("Enter Product Name: ")

# bug Validate and convert quantity to an integer
try:
    quantity = int(input("Enter the Quantity of the Product: "))
except ValueError:
    print("Invalid quantity. Please enter a whole number.")
    exit()

totalPrice = 0

#  bug Correctly match the product to its respective price
if productName == "headPhone":
    totalPrice = headPhone * quantity
elif productName == "smartWatch":
    totalPrice = smartWatch * quantity
elif productName == "PS5":
    totalPrice = PS5 * quantity
elif productName == "iPad":
    totalPrice = iPad * quantity
else:
    print("Product not found.")
    exit()

print(f"Total Amount To Be Paid: {totalPrice}")

# Electricity Bill Calculator
# Write a program that calculates the electricity bill based on units consumed using different rates for different slabs.

# 100 and below = 3
# 100-200 = 5
# 200-300 = 7
# 300 above = 10


units = int(input("Enter Units Consumed: "));

# bug Validate and convert units to an integer

if units <= 100:
    totalBill = units * 3;
#bug Correctly calculate the bill for units between 101 and 200
elif units <= 200:
    totalBill = 100*3 + (units-100)*5;

elif units <= 300:
    totalBill = 100*3 + 100*5 + (units-200)*7;

else:
    totalBill = 100*3 + 100*5 + 100*7 + (units-300)*10;


print(f"Total Electricity Bill: {totalBill}");
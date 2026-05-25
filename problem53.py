# Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria:

# above 100000 15% tax
# more then 50000 and less then 10000 10% tax
# less then 50000 5% tax
total=0
price=float(input("Enter your price: "))

if price>=100000:
    total=price*0.15
    print("Your total bill is:",total+price)

elif price>=50000 and price<=100000:
    total=price*0.10
    print("Your total bill is:",total+price)

elif price<=50000:
    total=price*0.5
    print("Your total bill is:",total+price)

print("Thank you")
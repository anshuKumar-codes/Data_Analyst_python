# Write a program to calculate the electricity bill based on the number of units consumed.
# - First 100 units → No charge
# - Next 100 units → ₹5 per unit
# - After 200 units → ₹10 per unit
# Example: If input = 350 units, bill = ₹2000
amt=0

a=float(input("Enter unit: "))

if a == 100:
    print("No charges ")

elif a>=100 and a<=200:
    amt=(a-100)*5
    print("Amount to pay: ",amt)

elif a>=200:
    amt=500+(a-200)*10
    print("Amount to pay:",amt)


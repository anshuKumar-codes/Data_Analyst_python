# wap a program to accept percentage from the user and display grade accoridng to the following criteria:

a=float(input("Enter your percentage: "))

if a>=90:
    print("Your grade is A:",a)

elif a>=80 and a<=90:
    print("Your grade is B:",a)

elif a>=60 and a<=90:
    print("Your grade is C:",a)

elif a<=60:
    print("Your grade is D",a)

print("Thank you")

# write a program to display the last digit of a negative number.

digit=0

a=int(input("Enter your number: "))

b=-(abs(a)%10)
digit=b
print("your last digit is:",digit)

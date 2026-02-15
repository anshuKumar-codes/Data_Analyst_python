# write a program to check whether the last digit of a number entered by the user is divisible by 3 or not.


digit=0

a=int(input("Enter your number: "))

b=a%10
digit=b
if digit%3==0:
    print("your number is divisble by 3")
else:
    print("your number is not divisble by 3")



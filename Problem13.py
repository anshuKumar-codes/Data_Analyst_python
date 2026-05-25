# palindrome number using while loop

i=int(input("Enter your number: "))
rev=0
x=i # Loop destroy the original i value thats why we give the value of i in x
while i>0:
    rev=(rev*10)+i%10
    i=i//10
if(x==rev):
    print("It is palindrome number")
else:
    print("It is not palindrome number")




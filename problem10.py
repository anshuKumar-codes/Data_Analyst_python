# WAP to find the factorial of first n numbers.(Using for loop)

a=int(input("Enter your number: "))

fact=1
for i in range(1,a):
    fact=fact*i
print(fact)
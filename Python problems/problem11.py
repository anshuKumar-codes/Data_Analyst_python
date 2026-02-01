# fibonacci series using while loop 

n=int(input("Enter your number"))
x=0
y=1

i=0
while(i<=n):
    print(i)
    x=y
    y=i
    i=x+y
   
    
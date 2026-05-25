# fibonacci series using For loop 

n=int(input("Enter your number: "))
x=0
y=1
print(x)
print(y)
for i in range(n):
    z=x+y
    print(z)
    x=y
    y=z
    
   
   
# create a new list take input from the user 

# for loop
# x=int(input("Enter the size of list: "))
# r=[]

# for i in range(0,x):
#     g=eval(input("Enter your list: "))
#     r.append(g)
# print(r)

# while loop   
x=int(input("Enter the size of list: "))
r=[]

i=0
while i < x:
    g=eval(input("Enter list: "))
    r.append(g)
    i=i+1
print(r)

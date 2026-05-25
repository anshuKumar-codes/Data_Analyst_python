# write a program to create a new list and when user give exit then use break and print the new list

x=int(input("Enter size of list: "))
r=[]
for i in range(0,x):
    g=input("Enter list: ")
    if g.lower()=="exit":
        break
    if g.isdigit():
        r.append(int(g))
    else:
        r.append(g)
print(r)
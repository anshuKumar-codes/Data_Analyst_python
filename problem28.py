# Delete the elements in the list element input by the user 

k=[1,2,3,4,5,6,7,8,9]

x=int(input("Enter size of list you want to delete: "))
for i in range(0,x):
    g=eval(input("Enter list: "))
    k.remove(g)
print(k)

        


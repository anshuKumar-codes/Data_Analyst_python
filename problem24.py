# Write a Python program to get the smallest number from a list.

a=[1,2,5,10,2,3]
print(min(a))

a=[1,2,5,10,2,3]
smallest=a[0]
for i in a:
    if i<smallest:
        smallest=i
print(smallest)
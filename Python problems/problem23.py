# Write a Python program to get the largest number from a list.

# a=[2,5,10,2,3]

# print(max(a))

a=[2,5,10,2,3]
largest=a[0]
for i in a:
    if i<largest:
        largest=i
print(largest)
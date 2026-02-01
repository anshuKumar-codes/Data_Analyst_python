a=[1,2,3,"Anshu","Chandan",44,55]
a.append(3) # it means that stores the value in the last of list
print(a)

b=[2,1,3] # when we use sort method it is compulsory our list is without ascending and desending order. 
# sort is using for ascending and desending to list.
b.sort() # sort() by default arrange our list in ascending order.
print(b)
b.sort(reverse=True) # sort(reverse=True) it is arrange list in desecding order
print(b)

c=["A","D","C","E"]
c.sort() # sort() for strings or characters values in the list arrange in ascending by the alphabets place numbers who comes first in alphabets
print(c)
c.sort(reverse=True) # Also arrange in descending list by the alphabets place numbers 
print(c)

d=["Anshu","Badal","Chandan",2,4,1]
d.reverse() # .reverse() is use for reverse the whole list.
print(d) 

e=["Anshu","Badal","Chandan",2,4,1]
e.insert(1,5) # .insert(index,n) insert element at index.
print(e)

f=[2,1,3,1]
f.remove(1) # removes first occurance of elements. when in the list has duplicate value then delete who comes first in index from the duplicate values.
print(f)

g=[2,1,3,1]
g.pop(0) # .pop(index) remove the elements in the list given index by the user.
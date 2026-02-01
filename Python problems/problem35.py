# count nested loop in the given list 
count=0
k=[1,2,3,[4,5,6],7,8,9,[10,11,12]]

for i in k:
    if isinstance(i,list):
        count+=1
print(count)




            
        


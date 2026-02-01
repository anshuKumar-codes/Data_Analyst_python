# write a program to find the prime no. in a list.
k=[1,2,3,4,5,6,7]
r=[]
for i in k:
    c=0
    for j in range(1,i+1):
        if i % j==0:
            c=c+1
    if c==2:
        r.append(i)
print(r)
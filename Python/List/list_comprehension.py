# ist comprehension syntax r=[expression for variable in iterator if condtion]

# r=[]

# for i in range(100):
#     if i%3==0:
#         r.append(i)
# print(r)

# r=[i for i in range(100) if i%3==0]
# print(r)

# h=[i for i in range(20) if i%2==0]
# p=[i for i in range(20) if i%3==0]
# print("Even list",h)
# print("Odd list",p)

# p=()
# c=[(x,y) for x in range(3) for y in range(3)]


k=[4,5,6,7,8,9]
k2=[1,2,3,4,10,11]

s=[i for i in k if i in k2]
print(s)
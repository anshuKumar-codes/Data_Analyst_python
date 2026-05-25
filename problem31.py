k=[3,"monu","anshu",4,"monu",5,6,7,8]
c=0
for i in range(0,len(k)):
    if k[i]=="monu":
        c=c+1
    if c==2:
        k[i]="Noida"
        break
print(k)


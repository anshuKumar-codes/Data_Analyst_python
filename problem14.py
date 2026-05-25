# armstrong number

i=int(input("Enter your number: "))
orig=i
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if(orig==sum):
    print("Armstrong number")
else:
    print("Not Armstrong number") 
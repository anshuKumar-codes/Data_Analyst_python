# check prime number or not.

num=int(input("Enter number: "))

if num>1:
    for i in range(2,num):
        if num%i==0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")
else:
    print("Number is not prime")
            
    



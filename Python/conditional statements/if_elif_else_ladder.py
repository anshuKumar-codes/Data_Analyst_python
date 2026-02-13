age=int(input("Enter your age: "))

if age>=18:
    print("You are the above the age of consent")

elif age>=0:
    print("invalid age")

elif age==0:
    print("Zero is not a age please enter valid age")
    
else:
    print("You are not above the age of consent")
age=int(input("Enter your age: "))

# if statement no: 1 (This if is independent)
if age%2==0:
    print("a is even")
# end of if statement no: 2

# if statement no: 2
if age>=18:
    print("You are the above the age of consent")

elif age<=0:
    print("invalid age")

elif age==0:
    print("Zero is not a age please enter valid age")
    
else:
    print("You are not above the age of consent")
# end of id statement no: 2
age1=int(input("Enter age 1: "))
age2=int(input("Enter age 2: "))
age3=int(input("Enter age 3: "))
age4=int(input("Enter age 4: "))

if age1>=age2 and age1>=age3 and age1>=age4:
    print("Age of oldest:",age1)
elif age2>=age1 and age2>=age3 and age2>=age4:
    print("Age of oldest:",age2)
elif age3>=age2 and age3>=age3 and age3>=age4:
    print("Age of oldest:",age1)
elif age4>=age1 and age4>=age2 and age4>=age3:
    print("Age of oldest:",age4)
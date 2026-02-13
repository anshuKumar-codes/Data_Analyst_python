# Simple calculator 

while True: # while true  “Keep running this block of code forever, until I manually stop it or break out of it.”
    print("1.ADD")
    print("2.SUB")
    print("3.MUL")
    print("4.DIV")
    print("5.SQUARE & CUBE")
    print("6.EXIT")


    x=int(input("Enter your choice: "))

    if x==1:
        a=int(input("Enter your first number: "))
        b=int(input("Enter your second number: "))
        c=a+b
        print("Sum is", c )
        
    elif x==2:
        a=int(input("Enter your first number: "))
        b=int(input("Enter your second number: "))
        c=a-b
        print("Sub is", c )

    elif x==3:
        a=int(input("Enter your first number: "))
        b=int(input("Enter your second number: "))
        c=a*b
        print("DIV is", c )

    elif x==4:
        a=int(input("Enter your first number: "))   
        b=int(input("Enter your second number: "))
        c=a/b
        print("DIV is", c )

    elif x==5:
        a=int(input("Enter your first number: "))   
        b=int(input("Enter your second number: "))
        if b==2:
            c=a**b
            print("Your sqaure is",c)
        elif b==3:
            c=a**b
            print("Your cube is",c)
        else:
            c=a**b
            print("Your numner is",c)
         
    elif x==6:
        print("Exit")
        break
    else:
        print("No choice")



        
    
        





    

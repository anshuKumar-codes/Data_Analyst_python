# WAP to accept a number from 1 to 7 and display the name of the day like 1 for sunday 2 for monday and so on.


num=int(input("Enter your number 1 to 7: "))

if num==1:
    print("Monday")
elif num==2:
    print("Tuesday")
elif num==3:
    print("Wednesday")
elif num==4:
    print("Thursday")
elif num==5:
    print("Friday")
elif num==6:
    print("Saturday")
elif num==7:
    print("Sunday")
else:
    print("Plese enter valid number")
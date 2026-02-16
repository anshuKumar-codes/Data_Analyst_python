# WAP to accept a number from 1 to 12 and display the name of the day like 1 for january 2 for febuary and so on.


num=int(input("Enter your number 1 to 12: "))

if num==1:
    print("January")
elif num==2:
    print("Febuary")
elif num==3:
    print("March")
elif num==4:
    print("April")
elif num==5:
    print("May")
elif num==6:
    print("june")
elif num==7:
    print("july")
elif num==8:
    print("August")
elif num==9:
    print("Septemver")
elif num==10:
    print("October")
elif num==11:
    print("November")
elif num==12:
    print("December")
else:
    print("Plese enter valid number")
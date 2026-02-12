# WAP to to check whether an years is leap year or not.

year=int(input("Enter year: "))

if year%4==0 or year%400==0:
    print("leap year:",year)

elif year%100==0:
    print("Not leap year:",year)



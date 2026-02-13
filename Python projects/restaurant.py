total=0

while True:
    print("1.Breakfast")
    print("2.Lunch")
    print("3.Snacks")
    print("4.Dinner")
    print("5.Exit")

    x=int(input("Enter your choice : "))
    if x==1: # Breakfast
        while True:
            print("1.Paratha-25")
            print("2.Poha - 40")
            print("3.Aloo puri-30")
            print("4.Upma - 60")
            print("5.Exit")
            a=int(input("Enter your choice on breakfast: "))
            if a==1: #prarathe-25
                q=int(input("Enter quantity: "))
                total=total+q*25
                print("your bill is ",total)
            elif a==2: #poha-40
                q=int(input("Enter Quantity: "))
                total=total+q*40
                print("your bill is ",total)
            elif a==3: #Aloo puri-30
                q=int(input("Enter quantity: "))
                total=total+q*30
                print("your bill is ",total)
            elif a==4: #Upma-60
                q=int(input("Enter quantity: "))
                total=total+q*60
                print("your bill is ",total)
            elif a==5:
                print("Exit")
            else:
                print("No choice")
            break
    

    elif x==2: #Lunch
        while True:
            print("1.Dal chawal - 50")
            print("2.Roti Sabji - 30")
            print("3 Chole Rice - 40")
            print("4.Rajma Rice - 60")
            print("5.Exit")
            a=int(input("Enter your choice on lunch: "))
            if a==1:#Dal chawal - 50
                q=int(input("Enter quantity: "))
                total=total+q*50
                print("Your bill is",total)
            elif a==2:#Roti Sabji - 30
                q=int(input("Enter your quantity: "))
                total=total+q*30
                print("Your bill is",total)
            elif a==3:#Chole Rice - 40
                q=int(input("Enter your quantity: "))
                total=total+q*40
                print("Your bill is",total)
            elif a==4:#Rajma Rice - 60
                q=int(input("Enter your quantity: "))
                total=total+q*60
                print("Your bill is",total)
            elif a==5:
                print("Exit")
            else:
                print("No choice")
            break
        


    elif x==3: #Snacks
        while True:
            print("1.Samosa - 10")
            print("2.Pakoda - 20")
            print("3.Chaat - 25")
            print("4.Dhokla - 10")
            print("5.Exit")
            a=int(input("Enter your choice in snacks: "))
            if a==1: # Samosa-10
                q=int(input("Enter quantity: "))
                total=total+q*10
                print("Your bill is",total)
            elif a==2: # Pakoda-20
                q=int(input("Enter quantity: "))
                total=total+q*20
                print("Your bill is",total)
            elif a==3: #Chaat-25
                q=int(input("Enter quantity: "))
                total=total+q*25
                print("Your bill is",total)
            elif a==4: #Dhokla - 10
                q=int(input("Enter quantity: "))
                total=total+q*10
                print("Your bill is",total)
            elif a==5:
                print("Exit")
            else:
                print("No choice")
            break

    elif x==4: # Dinner
        while True:
            print("1.Egg curry or roti - 70")
            print("2.Chicken Rice - 100")
            print("3.Mutton Roti- 120")
            print("4.Fish Curry or rice -90")
            print("5.Exit")
            a=int(input("Enter your choice in Dinner"))
            if a==1: # Egg curry or roti-70
                q=int(input("Enter quantity: "))
                total=total+q*70
                print("Your bill is",total)
            elif a==2: # Chicken Rice-100
                q=int(input("Enter quantity: "))
                total=total+q*100
                print("Your bill is",total)
            elif a==3: # Mutton Roti-120
                q=int(input("Enter quantity: "))
                total=total+q*70
                print("Your bill is",total)
            elif a==4: # Fish Curry or rice-90
                q=int(input("Enter quantity: "))
                total=total+q*90
                print("Your bill is",total)
            elif a==5:
                print("Exit")
            else:
                print("No choice")
            break
    
    elif x==5:
        print("Exit")
    else:
        print("No choice")
        break
        


    


    
    

    
    
    
    
    



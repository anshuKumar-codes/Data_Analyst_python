total=0
while True:

    print("Choose App for movie ticket")
    print("1.District")
    print("2.Paytm movies")
    print("3.Book my show")
    print("4.PVR cinemas")
    print("5.Exit")
    x=int(input("Enter your app for movie ticket: "))
    if x==1:

        while True:
            print("choose Theater")
            print("1.Silver city ")
            print("2.Opulent PVR")
            print("3.Gaucity")
            print("4.Sipra")
            print("5.Exit") 
            a=int(input("Enter your location: "))
            if a==1:

                while True:
                    print("Now Showing silver city movies ")
                    print("1.Dhurandhar")
                    print("2.Border 2")
                    print("3.Avatar:Rise and Fall")
                    print("4.Raja Sahab")
                    print("5.Exit")
                    b=int(input("Enter your movies to watch: "))
                    if b==1:
                        
                        while True:
                            print("Choose Show time")
                            print("1.Morning show At 10 AM")
                            print("2.Afternoon show at 2 PM large screening")
                            print("3.Evening Show at 6 PM")
                            print("4.Night show at 10 PM")
                            print("5.Exit")
                            c=int(input("choose your Timing: "))
                            if c==1:
                                
                                while True:
                                    print("Choose seat categories")
                                    print("1.Platinum-200+18%GST")
                                    print("2.Gold-150+18%GST")
                                    print("3.Silver-100+18%GST")
                                    print("4.Exit")
                                    d=int(input("Enter your seat location: "))
                                    if d==1:
                                        num=int(input("Enter Number of seats: "))
                                        total=total+num*(200+(200*18/100))
                                        print("Your total bill is including 18%GST",total)
                                    elif d==2:
                                        num=int(input("Enter Number of seats: "))
                                        total=total+num*(150+(150*18/100))
                                        print("Your total bill is including 18%GST",total)
                                    elif d==3:
                                        num=int(input("Enter Number of seats: "))
                                        total=total+num*(100+(100*18/100))
                                        print("Your total bill is including 18%GST",total)
                                    elif d==4:
                                        print("Exit")    
                                    else:
                                        ("No choice")
                                    break
                            break

                    break

            break                                
            
                                    
    
    elif x==2:

        while True:
            print("choose Theater")
            print("1.Silver city ")
            print("2.Opulent PVR")
            print("3.Gaucity")
            print("4.Sipra")
            print("5.Exit") 
            a=int(input("Enter your location: "))
            if a==2:

                while True:
                    print("Now Showing Opulent PVR movies ")
                    print("1.Dhurandhar")
                    print("2.Border 2")
                    print("3.Avatar:Rise and Fall")
                    print("4.Raja Sahab")
                    print("5.Exit")
                    b=int(input("Enter your movies to watch: "))
                    if b==2:
                        
                        while True:
                            print("Choose Show time")
                            print("1.Morning show At 10 AM")
                            print("2.Afternoon show at 2 PM largest screening")
                            print("3.Evening Show at 6 PM")
                            print("4.Night show at 10 PM")
                            print("5.Exit")
                            c=int(input("choose your Timing: "))
                            if c==2:
                                
                                while True:
                                    print("Choose seat categories")
                                    print("1.Platinum-250+18%GST")
                                    print("2.Gold-200+18%GST")
                                    print("3.Silver-150+18%GST")
                                    print("4.Exit")
                                    d=int(input("Enter your seat categories: "))
                                    if d==1:
                                        num=int(input("Enter Number of seats: "))
                                        total=total+num*(250+(250*18/100))
                                        print("Your total bill is including 18%GST",total)
                                    elif d==2:
                                        num=int(input("Enter Number of seats: "))
                                        total=total+num*(200+(200*18/100))
                                        print("Your total bill is including 18%GST",total)
                                    elif d==3:
                                        num=int(input("Enter Number of seats: "))
                                        total=total+num*(150+(150*18/100))
                                        print("Your total bill is including 18%GST",total)
                                    elif d==4:
                                        print("Exit")
                                        break
                                    else:
                                        print("No choice")
                         
                                    break
                            break

                    break
            break

    
    elif x==3:

        while True:
            print("choose Theater")
            print("1.Silver city ")
            print("2.Opulent PVR")
            print("3.Gaucity")
            print("4.Sipra")
            print("5.Exit") 
            a=int(input("Enter your location: "))
            if a==3:

                while True:
                    print("Now Showing Opulent PVR movies ")
                    print("1.Dhurandhar")
                    print("2.Border 2")
                    print("3.Avatar:Rise and Fall")
                    print("4.Raja Sahab")
                    print("5.Exit")
                    b=int(input("Enter your movies to watch: "))
                    if b==3:
                        
                        while True:
                            print("Choose Show time")
                            print("1.Morning show At 10 AM")
                            print("2.Afternoon show at 2 PM largest screening")
                            print("3.Evening Show at 6 PM")
                            print("4.Night show at 10 PM")
                            print("5.Exit")
                            c=int(input("choose your Timing: "))
                            if c==3:
                                
                                while True:
                                    print("Choose seat categories")
                                    print("1.Platinum-300+18%GST")
                                    print("2.Gold-250+18%GST")
                                    print("3.Silver-200+18%GST")
                                    print("4.Exit")
                                    d=int(input("Enter your seat location: "))
                                    if d==1:
                                        num=int(input("Enter Number of seats: "))
                                        total=total+num*(300+(300*18/100))
                                        print("Your total bill is including 18%GST",total)
                                    elif d==2:
                                        num=int(input("Enter Number of seats: "))
                                        total=total+num*(250+(250*18/100))
                                        print("Your total bill is including 18%GST",total)
                                    elif d==3:
                                        num=int(input("Enter Number of seats: "))
                                        total=total+num*(200+(500*18/100))
                                        print("Your total bill is including 18%GST",total)
                                    elif d==4:
                                        print("Exit")
                                        break
                                    else:
                                        print("No choice")
                         
                                    break
                            break

                    break
            break
    
    elif x==4:

        while True:
            print("choose Theater")
            print("1.Silver city ")
            print("2.Opulent PVR")
            print("3.Gaucity")
            print("4.Sipra")
            print("5.Exit") 
            a=int(input("Enter your location: "))
            if a==4:

                while True:
                    print("Now Showing Opulent PVR movies ")
                    print("1.Dhurandhar")
                    print("2.Border 2")
                    print("3.Avatar:Rise and Fall")
                    print("4.Raja Sahab")
                    print("5.Exit")
                    b=int(input("Enter your movies to watch: "))
                    if b==4:
                        
                        while True:
                            print("Choose Show time")
                            print("1.Morning show At 10 AM")
                            print("2.Afternoon show at 2 PM largest screening")
                            print("3.Evening Show at 6 PM")
                            print("4.Night show at 10 PM")
                            print("5.Exit")
                            c=int(input("choose your Timing: "))
                            if c==4:
                                
                                while True:
                                    print("Choose seat categories")
                                    print("1.Platinum-500+18%GST")
                                    print("2.Gold-400+18%GST")
                                    print("3.Silver-350+18%GST")
                                    print("4.Exit")
                                    d=int(input("Enter your seat location: "))
                                    if d==1:
                                        num=int(input("Enter Number of seats: "))
                                        total=total+num*(500+(500*18/100))
                                        print("Your total bill is including 18%GST",total)
                                    elif d==2:
                                        num=int(input("Enter Number of seats: "))
                                        total=total+num*(400+(400*18/100))
                                        print("Your total bill is including 18%GST",total)
                                    elif d==3:
                                        num=int(input("Enter Number of seats: "))
                                        total=total+num*(350+(350*18/100))
                                        print("Your total bill is including 18%GST",total)
                                    elif d==4:
                                        print("Exit")
                                        break
                                    else:
                                        print("No choice")
                         
                                    break
                            break

                    break
            break
    
    elif x==5:
        print("Exit")
    else:
        print("No choice")
    

                             
        
            
                                    



                        






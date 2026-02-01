"""
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

"""
for i in range(1,6):
    for j in range(5-i): # 5 is total row and i is current row
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()

        



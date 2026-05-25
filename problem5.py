# search for a number x in this tuple using while loop:
# (1,4,9,16,25,36,49,64,81,100)


a = (1,4,9,16,25,36,49,64,81,100)

x=16

idx = 0
while idx < len(a):
    if(a[idx]==x):
        print("Found at idx",idx)
        
    
    idx+=1
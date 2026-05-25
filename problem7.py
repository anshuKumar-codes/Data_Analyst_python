# search the number x in the tuple using loop

a=(1,2,3,4,5,6,7,8,9,10) # Ye ek tuple hai 
x=5 # Tuple mai se number 10 find karna hai 
idx=0 # iska matlab index shuru ho rha hai 0 se

for i in a:
    if(i==x):
        print("number found at index",idx)
    idx+=1
    

# recursive function
def show(n):
    if(n==0):
        return # base case
    print(n)
    show(n-1)

show(3) 
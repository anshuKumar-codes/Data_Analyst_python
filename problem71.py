def calculate(a,b,o):
    if o=="+":
        return a+b
    elif o=="-":
        return a-b
    elif o=="*":
        return a*b
    elif o=="/":
        return a/b
    else:
        return "enter valid operations"


sum=calculate(1,2,"+")
print(sum)
def maximum(a,b,c):
    if a>b and a>c:
        return "a is maximum"
    elif b>a and b>c:
        return "b is maximum"
    elif c>a and c>b:
        return "c is maximum"
    else:
        return "Thank you"
value=maximum(1,2,3)
print(value)
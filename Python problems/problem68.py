# WAF to find even or odd input from user

a=int(input("Enter your number: "))
def even_odd(a):
    if a%2==0:
        print(" Number is Even")
    else:
        print("Number is odd")
even_odd(a)

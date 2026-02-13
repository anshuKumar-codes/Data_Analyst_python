# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. 

a=input("Enter message: ")

if a == "Make a lot of money" or a == "buy now" or a =="subscribe this" or a == "click this":
    print("this is a spam message")
else:
    print("This is secure message")
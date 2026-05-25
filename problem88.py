# You have to take an interger input a, and then use the if statement to print "Big" (without quotes) if the given number is greater than 100, 
# and use the else statement to print "Small" (without quotes) when the number is smaller than or equal to 100.

# a=int(input("Enter your number: "))

# if a>=100:
#     print("big")
# else:
#     print("small")


# # Write a program to create a new string made of an input string’s first, middle, and last characters.
# a=input("Enter name: ")
# new_middle=len(a) // 2 

# new_str=a[0] + a[new_middle] + a[-1]
# print(new_str)

# s1="Ault"
# mi = len(s1) // 2
# print(type(a))


str1=input("Enter str1: ")
str2=input("Enter str2: ")

mi1=(len(str1)//2)
mi2=(len(str2)//2)

new_str = str1[0] + str1[mi1] + str1[-1] + str2[0] + str2[mi2] + str2[-1]
print(new_str)
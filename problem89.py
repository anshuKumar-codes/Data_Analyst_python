# str=input("Enter your str")
# print(len(str))

# text=input("Enter your str: ")
# count=0
# vowels="aeiouAEIOU"

# for char in text:
#     if char in vowels:
#         count+=1
# print("numbers of vowels: ",count)



# text=input("Enter your text: ")
# reverse_text=text[-1:-6:-1]

# text=input("Enter your text: ")
# reverse_text=text[ : :-1 ]

# if reverse_text==text:
#     print("The string is palindrome",text)
# else:
#     print("The string is no palindrome",text)
    

str=input("Enter your text: ")
count=0
for char in str:
    if char.lower==str:
        count+=1
print(count)
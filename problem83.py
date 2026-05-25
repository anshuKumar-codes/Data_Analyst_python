#WAP to check if a list contains a palindrome of element.(Hint:use copy()method)

list=[1,2,3]
copy=list.copy()
copy.reverse()

if copy==list:
    print("Palindrome list")
else:
    print("Not Palindrome list")
    

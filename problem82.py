# # WAP to ask the user to enter name of their 3 favourite movies and store them in a list.
# movies=[]
# movie1=input("Enter your favourite movie:")
# movie2=input("Enter your favourite movie:")
# movie3=input("Enter your favourite movie:")

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)

# print(movies)

list=[1,2,3,2,3]

copy=list.copy()
copy.reverse()

if copy==list:
    print("palindrome list")
else:
    print("Not palindrome list")

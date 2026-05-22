# List Item Exchanger (Lists)

# Task: Create a list with two elements, e.g., [10, 20]. Write a program that swaps their positions so the list becomes [20, 10].

# Requirement: Do this without just re-typing the list. Use indexing or a temporary variable.

list=[10,20]

temp=list[0]
list[0]=list[1]
list[1]=temp
print(list)

s={1,2,3,4,"Manish","Anshu",345,4,5,6}
s2={3,2,66,7,"Anshu","Aadil"}

# print(s.intersection(s2)) # Common value.
# print(s.union(s2)) # Only contain unique value and remove duplicate value.

# s.clear() # Clear all the value in the set. 
# print(s)

# print(s.issubset(s2)) # issubset means that Is child set element are present in parent set.

# s.remove("Anshu") # remove method is use for remove the Asign elements from the set.
# print(s)

# s.discard("Chandan") # discard is use when asign value is present in the set then remove and also asign value is not given then cannot give error.
# print(s)

s.update(s2)
print(s)


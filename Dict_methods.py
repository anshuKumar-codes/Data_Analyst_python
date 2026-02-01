marks={"Anshu":100,"Manish": 50,"Shubham": 100}
# print(marks.items()) # to print dictionary with pair of key and values and in the form of tuple.

# print(marks.values()) # it only return values 

# print(marks.keys()) # it only return keys 

# marks.update({"Anshu":90,"Manish":80}) # Update the values in dictionary.
# # when we update key then by default it insert on the last.
# print(marks)

# print(marks.get("Anshu2")) # prints None
# print(marks["Anshu2"]) # Return error

# marks.pop("Anshu") # remove the key and 
# print(marks)

# marks.popitem() # by default it removes the last index in dictionary
# print(marks)

# marks.clear() # clear all the 
# print(marks)

# keys=["a","b","c"] # we asign the key
# new_dict=dict.fromkeys(keys,0)# keys are stored and value are zero
# print(new_dict)

# marks.copy() # return copy of dictionary
# print(marks)


# list slicing is done with indexs [0,1,2,.....,-nth]
# list slicing also done with negative index and negative index considered on the backward of list [-nth,......,-4,-3,-2,-1]

list=["Anshu",99,99.0,'A',True,False]
print(list[1:4]) # it print list according to their indexs 
print(list[:4]) # we cannot assing starting index in list then by default it considered 0th index automatically 
print(list[1:]) # similarly we cannot assing last index by default it considered total lenght of index(n th index)
print(list[0:4:1]) # this called step list is print but drop step 1 
# [1] list Items Are Enclosed in Square Brackets
# [2] list Are Ordered, To Use Index To Acces Item
# [3] list Are Mutable => Add, Delete, Edit
# [4] list Items Is not unique
# [5] list can have different data types

My_List=["One","Two","tree",1,100.5,True]

print("print all the list : ",My_List) # whole list
print("print index 0 : ",My_List[0]) # "one"
print("print index -1 : ",My_List[-1]) # True
print("print index -3 : ",My_List[-3]) # 1

print("List from index 1 to 4 : ",My_List[1:4]) # "Two" , "One" ,1  
print("List from start to 4 : ",My_List[:4]) # "One","Two","tree",1
print("List from index 1 to end : ",My_List[1:]) # "Two","tree",1,100.5,True

print("Print List by 1 step : ",My_List[::1]) # 'One', 'Two', 'tree', 1, 100.5, True
print("print List by 2 steps : ",My_List[::2]) # 'One', 'tree', 100.5

My_List[1]=44
print("list after changing : ",My_List)

My_List[0:3]=["str_numbers"]
print("list after changing : ",My_List)

My_List[0:7]=[]
print("Empty the list : ",My_List)





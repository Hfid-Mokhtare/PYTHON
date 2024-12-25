
# ---------------------
# --- Lists Methods ---
# ---------------------

# append()

My_List=["ali","Mohamed","rida"]
My_List_2=["QQ","AA","ZZ"]

print("print all the list : ",My_List) # whole list

My_List.append("yahya")
My_List.append(1)
My_List.append(10.5)
My_List.append(True)
My_List.append(My_List_2)

print("print all the list after append : ",My_List) # whole list
print("print the element in the inside list : ",My_List[7][2])

# extend()

a=[1,2,3,4]
b=['a','b','c']
a.extend(b)
print("print all the list after extend : ",a)

# remove()

x=[1,2,3,4,5,"Ali","Ali","Mohamed"]
x.remove("Ali")
print(x)

# sort()

z=["a","b","c"]
y=[5,1,44,3,2,12,33]
y.sort(reverse=True)
z.sort(reverse=True)
print(y,z)

# reverse()

c=["a","b","c"]
c.reverse()
print(c)

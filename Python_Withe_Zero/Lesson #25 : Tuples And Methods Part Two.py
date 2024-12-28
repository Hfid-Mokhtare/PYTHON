# ------------------
# ---- Tuple -------
# ------------------

# Tuple withe one element : you have to add a coma

MyTuple1=("Ali",)
MyTuple2= "Ali",

print(type(MyTuple1))
print(type(MyTuple2))

print(len(MyTuple1))
print(len(MyTuple2))

# Tuple Concatenation

a=(1,2,3,4,5,6,7)
b=(8,9,10)

c= a+("ali",)+b
print(c)

# Tuple Muliplication
d=(8,9,10)
print(d*5)

# Methods => count()

tuple_c=(1,2,3,4,5,4,7)
print(tuple_c.count(4))

# Methods => index()

tuple_i=(1,2,3,4,5,4,7)
print(f"the index 4 is : {tuple_i.index(4)}")

# Tuple Destruct
tuple_a=("A","B",4,"C")
A,B,C ="A","B","C"
X,Y, _, Z =tuple_a

print(A)
print(B)
print(C)

print(X)
print(Y)
print(Z)

 

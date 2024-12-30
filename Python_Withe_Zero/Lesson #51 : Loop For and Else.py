# ------------------------------
# -------- Loop => For----------
# ------------------------------

# for item in iterable_object : 
#   Do something with Item

#-------------------------------


MyNumbers=[1,2,3,4,5]

for Num in MyNumbers:
    if (Num % 2) != 0:
        print(Num,"is Odd")
    else: 
        print(Num,"is even")
else: 
  print("the Loop is coplited")

name="ali"
length=len(name)
for letter in name:
    print(letter.upper())

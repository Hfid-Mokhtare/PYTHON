# ------------------------------
# -------- Dictionary Methods --
# ------------------------------

user ={
    "first_name" : "mohamed ali",
    "age" : 36,
    "country" : "Morocco",
    "skills" : ["html","css","js"],
    "scorre": 10.5,
    
}

# clear()

print("-" * 50)

print(user)
user.clear()
print(user)

print("-" * 50)

# update()

user["last_name"]="zeggaf"
print(user)
user.update({"Note": 17})
print(user)

print("-" * 50)

# copy()
user2=user.copy()
user2.update({"class":"DEV 101"})
print(user2)

print("-" * 50)

# keys() + values()  
print(user.keys())
print(user.values())


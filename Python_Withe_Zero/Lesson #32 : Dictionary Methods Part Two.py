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

# setdefault()

print("-" * 50)


print(user.setdefault("last_name","zeggaf"))
print(user)


# popitem()

print("-" * 50)

print(user)
user.popitem()
print(user)

print("-" * 50)

# items()

print(user.items())


print("-" * 50)

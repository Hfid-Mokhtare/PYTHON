# ------------------------------
# -------- Dictionary -------
# ------------------------------

# [1] Dict Items are enclosed in curly braces
# [2] Dict Items Are contains Key : Value
# [3] Dict Key need to be immutable => (Number,string, tuple) list not allowed
# [4] Dict Value can have any data types
# [5] Dict Key need to be unique
# [6] Dict is not ordered you access its element with key
# [7] 
# --------------------------------------------------------------

user ={
    "name" : "ali",
    "age" : 36,
    "country" : "Morocco",
    "skills" : ["html","css","js"],
    "scorre": 10.5,
    "name" : "mohamed",
}

print(user)

print(user["country"])
print(user.get("name"))

# to print Keys
print(user.keys())

# to print Values
print(user.values())

# Two-Dimensional Dictionary

Programming_Languages={
    "back_end" : {
        "name": "C++",
        "Progress": "80%",
    },
    "front_end" : {
        "name": "Html",
        "Progress": "70%",
    },
    "Data": {
        "name": "MySql",
        "Progress" : "10%",
    }
}


print(Programming_Languages)
print(f"front end tetails : \nname of technologie : {Programming_Languages["front_end"]["name"]}")
print(f"my progress in technologie is  : {Programming_Languages["front_end"]["Progress"]}")

# print the length of Dict

print(f"in all dictionary i have {len(Programming_Languages)} element(s)")
print(Programming_Languages.keys())
print(f"and in data language i have {len(Programming_Languages["Data"])} element(s)")
print(Programming_Languages["Data"])

# change the value of Items in Dict

Programming_Languages["Data"]["name"]="No_SQL"
print(Programming_Languages["Data"])

personal_info={
    "first_name": "Mohamed Ali",
    "last_name" : "zeggaf",
    "age": 19,
    "country" : "morcco",
    "city" : "tangier"
}

contact_info={
    "phone_number": "0622705149",
    "adress {country-city-stryte}" : "Morocco-tangier-mghogha",
    "email": "mohamedalizeggaf@gmail.com",
    "facbook" : "Mohamed ali"
}
banck_info={
    "ID": "X1234",
    "Salair" : "1000",
    "acount_name": "Mohamed ali",
    "acount_number" : "5678 2690 2234"
}


client_info={
    "personal_info" : personal_info,
    "contact_info" : contact_info,
    "banck_info" : banck_info
}

print(client_info)

 

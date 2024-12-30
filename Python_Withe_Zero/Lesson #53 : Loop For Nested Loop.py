# ------------------------------
# -------- Loop => For----------
# -------- Nested Loop----------
# ------------------------------

# 

peoples=["ali","Mohamed ali","Reda","yassir","ahmad"]
skills=["HTML","CSS","JS"]

for name  in peoples: 
    print(f"{name} skills are :")
    for skill in skills: 
        print(f"-{skill}")

technologies={
    "back_end" : {
        "name": "C++",
        "Progress": "80%"
    },
    "front_end" : {
        "name": "Html",
        "Progress": "70%"
    },
    "Data": {
        "name": "MySql",
        "Progress" : "10%"
    }
}    

for technologie  in technologies: 
    print(f"I learned {technologie} : ")
    for language in technologies[technologie]: 
        print(f"-{language} ==> {technologies[technologie][language].upper()}  " )

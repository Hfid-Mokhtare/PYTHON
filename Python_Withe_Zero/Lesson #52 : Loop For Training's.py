# ------------------------------
# -------- Loop => For----------
# -------- Trainings----------
# ------------------------------

# Range

MyRange=range(1,101)

for num in MyRange:
    print(num)

print("-"*50)
# Dictionary
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

for technologie in Programming_Languages:
    print(f"i'm studying {technologie} and my progress on it is : {Programming_Languages[technologie]["Progress"]}")

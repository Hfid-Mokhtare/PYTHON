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
        
def print_Data(Data_technologies):
    for technologie_key, technologie_value  in Data_technologies.items(): 
        print(f"I learned {technologie_key} : ")
        for language_key, language_value in technologie_value.items(): 
            print(f"-{language_key} ==> {language_value.upper()}  " )

print_Data(technologies)

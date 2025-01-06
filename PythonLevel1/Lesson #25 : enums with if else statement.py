# you can use the class : 
# class Day(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7



# like an enum of days
monday = 1
tuesday = 2  
wednesday = 3 
thursday = 4
friday = 5
saturday = 6
sunday = 7

def ReadNumberOfDay():
    Day=int(input("Please enter the Number of a Day : "))
    return Day


def CheckGrade(NumDay):
    if NumDay == monday : 
       print("monday")
    elif NumDay == tuesday:
       print("tusday")
    elif NumDay == wednesday:
       print("wedensday")   
    elif NumDay == thursday:
       print("thursday") 
    elif NumDay == friday:
       print("friday")
    elif NumDay == saturday:
       print("saturday")
    elif NumDay == saturday:
       print("saturday")
    else :
       print("wrongue Input :( ")  

CheckGrade(ReadNumberOfDay())

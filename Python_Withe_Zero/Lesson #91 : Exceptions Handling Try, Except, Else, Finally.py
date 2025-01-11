#-----------------------------------
#-- Exceptions Handling ------------
#-- Try | Except | Else | Finally
#-----------------------------------

# Try  ==> Test the code for Errors
# Except ==> handle The Errors
#----------------------------------------------------

# Else  ==> if no errors
# Finally ==> run the code

#----------------------------------------------------

try:
    
    print(Num)
    Name=int(input("Please enter your name : "))
    print(10/0)
    
except NameError:
    print("you dont definde the variable")
except ValueError:
    print("the input is not correcte")
except ZeroDivisionError:
    print("there is a zero division error")


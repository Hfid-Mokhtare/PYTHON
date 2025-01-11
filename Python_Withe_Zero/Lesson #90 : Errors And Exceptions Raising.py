#----------------------------------------------------
#-- Errors And Exceptions Raising ------------
#---------------------------------------------

# [1] Exception Gives you the message to understand the problem
# [2] Exception have types (SyntaxError, IndexError, KeyError, etc...)
# [3] raise keyword used to raise you own exceptions

#----------------------------------------------------

Num=10

if Num<0:
    raise Exception("the number is negative ")
    # no code run after raise 
    print ("this line will not be printed")
else: 
    if type(Num) != str:
        raise ValueError("this is not a string ")
    print("the number is positive ")

#----------------------------------------------------


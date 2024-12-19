#Q1 : 

LoanAmount=int(input("please enter the Loan Amount :"))
manths_to_pay=int(input("please enter the MonthlyPayment :"))

calculate_MonthlyPayment_to_pay = LoanAmount // manths_to_pay

print(calculate_MonthlyPayment_to_pay,"\n")

#--------------------------------------------------------------------
#Q2 : 

Days:int=None
Hours:int=None
Minutes:int=None
Seconds:int=None
Task_duration_in_seconds:int=None
Remainder:float=None

Task_duration_in_seconds=int(input("please enter theTask duration in seconds :"))

Days=Task_duration_in_seconds // (24 * 60 * 60)
Remainder = Task_duration_in_seconds % (24 * 60 * 60)

Hours = Remainder // (60 * 60)
Remainder = Remainder % (60 * 60)

Minutes = Remainder // 60
Remainder = Remainder % 60

Seconds = Remainder

print( Days , ":" , Hours , ":" , Minutes , ":" , Seconds , ":" )

#--------------------------------------------------------------------
#Q3 : 

Num=int(input("Please enter a number : "))

result = pow(Num,2)
print(result)


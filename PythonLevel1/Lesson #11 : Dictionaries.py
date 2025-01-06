# using dictionary and for loop ------------------------------------------------------------------------

ContacteInfo={
    "facebook_acounte":str,
    "tweeter_acounte":str,
    "emaile":str,
    "phone":str
}

PersonalInfo={
    "FullName":str,
    "Age":int,
    "gender":chr

}

CartInfo={
    "ContacteInfo":ContacteInfo,
    "PersonalInfo":PersonalInfo
}

for data_k, data_v in CartInfo.items():
    for info_k in data_v:

        data_v[info_k]=input(f"enter {info_k} : ")

print("-"*50)

for data_k, data_v in CartInfo.items():
    for info_k, info_v in data_v.items():

        print(f"{info_k} : {info_v}")

#------------------------------------------------

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(person["name"])  # Output: Alice
print(person["age"])   # Output: 30


# Define classes to represent the information structures

class ConracteInfo: 
    def __init__(self,facebook_acounte,tweeter_acounte,amail,phone):
        self.facebook_acounte=facebook_acounte
        self.tweeter_acounte=tweeter_acounte
        self.email=amail
        self.phone=phone

class PersonalInfo: 
    def __init__(self,FullName,age,Gender,Married,MonthSalary):
        self.FullName=FullName
        self.age=age
        self.Gender=Gender 
        self.Married=Married
        self.MonthSalary=MonthSalary  
        # self.YearSalary:int=int(MonthSalary * 12)

class Adress: 
    def __init__(self,Country,City,Street):
        self.Country=Country
        self.City=City
        self.Street=Street

class MyCartInfo: 
    def __init__(self):
        self.Adress=Adress(None,None,None)
        self.ContacteInfo=ConracteInfo(None,None,None,None)
        self.PersonalInfo=PersonalInfo(None,None,None,None,None)

def main():
    My_Cart_Info=MyCartInfo()

    print("--------------------Read Information--------------------\n")

    #Read Personal Informations

    My_Cart_Info.PersonalInfo.FullName=input("Enter your Full Name : ")
    My_Cart_Info.PersonalInfo.age=int(input("Enter your Age : "))
    My_Cart_Info.PersonalInfo.Gender=input("Enter Your Gender (M/F)")
    My_Cart_Info.PersonalInfo.Married=bool(int(input("Are you Married (1/0)")))
    My_Cart_Info.PersonalInfo.MonthSalary=int(input("Enter Your Month Salary : "))

    #Read Adress Informations

    My_Cart_Info.Adress.Country=input("Enter your Country : ")
    My_Cart_Info.Adress.City=input("Enter your City : ")
    My_Cart_Info.Adress.Street=input("Enter Your Street Name : ")
  
    #Read ContacteInfo Informations

    My_Cart_Info.ContacteInfo.facebook_acounte=input("Enter your Facebook Acounte : ")
    My_Cart_Info.ContacteInfo.tweeter_acounte=input("Enter your Tweeter Acounte : ")
    My_Cart_Info.ContacteInfo.email=input("Enter Your Email : ")
    My_Cart_Info.ContacteInfo.phone=input("Enter Your Phone Number : ")
   
    print("--------------------Print Carte Information--------------------\n")

    print ("+----------------------------------------------------+")
    print ("\t\tYour Carte Information")
    print ("+----------------------------------------------------+")

    print("\tFullName:", My_Cart_Info.PersonalInfo.FullName)
    print("\tage:", My_Cart_Info.PersonalInfo.age)
    print("\tGender (M/F):", My_Cart_Info.PersonalInfo.Gender)
    print("\tMarried (1/0):", My_Cart_Info.PersonalInfo.Married)
    print("\tMonthSalary:", My_Cart_Info.PersonalInfo.MonthSalary)
    print("\tCountry:", My_Cart_Info.Adress.Country)
    print("\tCity:", My_Cart_Info.Adress.City)
    print("\tstreet:", My_Cart_Info.Adress.Street)
    print("\tFacebook_account:", My_Cart_Info.ContacteInfo.facebook_acounte)
    print("\ttweeter_account:", My_Cart_Info.ContacteInfo.tweeter_acounte)
    print("\temail:", My_Cart_Info.ContacteInfo.email)
    print("\tphone:", My_Cart_Info.ContacteInfo.phone)

main()




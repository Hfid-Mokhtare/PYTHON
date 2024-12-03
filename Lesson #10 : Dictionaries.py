person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(person["name"])  # Output: Alice
print(person["age"])   # Output: 30

#------------------------------------------------

# Define classes to represent the information structures

class ContactInfo:
  def __init__(self, facebook_account, twitter_account, email, phone):
    self.facebook_account = facebook_account
    self.twitter_account = twitter_account
    self.email = email
    self.phone = phone

class PersonalInfo:
  def __init__(self, full_name, age, gender, married, month_salary):
    self.full_name = full_name
    self.age = age
    self.gender = gender
    self.married = married
    self.month_salary = month_salary

class Address:
  def __init__(self, country, city, street):
    self.country = country
    self.city = city
    self.street = street

class MyCartInfo:
  def __init__(self):
    self.address = Address(None, None, None)  # Initialize with None values
    self.contact_info = ContactInfo(None, None, None, None)
    self.personal_info = PersonalInfo(None, None, None, None, None)

def main():
  my_cart_info = MyCartInfo()

  print("(((())))(((((())))))((())(()))))(())))()))))(((((())))\n")
  my_cart_info.personal_info.full_name = input("Enter your FullName: ")
  my_cart_info.personal_info.age = int(input("Enter your age: "))
  my_cart_info.personal_info.gender = input("Enter your Gender (M/F): ")[0].upper()  # Get first char as uppercase
  my_cart_info.personal_info.married = bool(int(input("Enter your Married (1/0): ")))  # Convert to bool
  my_cart_info.personal_info.month_salary = int(input("Enter your MonthSalary: "))

  my_cart_info.address.country = input("Enter your Country: ")
  my_cart_info.address.city = input("Enter your City: ")
  my_cart_info.address.street = input("Enter your street: ")

  my_cart_info.contact_info.facebook_account = input("Enter your Facebook_account: ")
  my_cart_info.contact_info.twitter_account = input("Enter your tweeter_account: ")
  my_cart_info.contact_info.email = input("Enter your email: ")
  my_cart_info.contact_info.phone = input("Enter your phone: ")
  print("(((())))(((((())))))((())(()))))(())))()))))(((((())))\n")

  print(" FullName:", my_cart_info.personal_info.full_name)
  print(" age:", my_cart_info.personal_info.age)
  print(" Gender (M/F):", my_cart_info.personal_info.gender)
  print(" Married (1/0):", my_cart_info.personal_info.married)
  print(" MonthSalary:", my_cart_info.personal_info.month_salary)
  print(" Country:", my_cart_info.address.country)
  print(" City:", my_cart_info.address.city)
  print(" street:", my_cart_info.address.street)
  print(" Facebook_account:", my_cart_info.contact_info.facebook_account)
  print(" tweeter_account:", my_cart_info.contact_info.twitter_account)
  print(" email:", my_cart_info.contact_info.email)
  print(" phone:", my_cart_info.contact_info.phone)

if __name__ == "__main__":
  main()

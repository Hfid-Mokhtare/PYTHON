from enum import Enum

class Color(Enum):
    Red = "Red"
    Green = "Green"
    Yellow = "Yellow"
    Blue = "Blue"

class Gender(Enum):
    Male = "Male"
    Female = "Female"

class MaritalStatus(Enum):
    Single = "Single"
    Married = "Married"

class Address:
    def __init__(self, street_name, building_no, po_box, zip_code):
        self.street_name = street_name
        self.building_no = building_no
        self.po_box = po_box
        self.zip_code = zip_code

class ContactInfo:
    def __init__(self, phone, email, address):
        self.phone = phone
        self.email = email
        self.address = address

class Person:
    def __init__(self, first_name, last_name, contact_info, gender, marital_status, favorite_color):
        self.first_name = first_name
        self.last_name = last_name
        self.contact_info = contact_info
        self.gender = gender
        self.marital_status = marital_status
        self.favorite_color = favorite_color

# Function to read user input
def read_person_info():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    street_name = input("Enter street name: ")
    building_no = input("Enter building number: ")
    po_box = input("Enter PO Box: ")
    zip_code = input("Enter ZIP code: ")
    gender_str = input("Enter gender (Male/Female): ")
    marital_status_str = input("Enter marital status (Single/Married): ")
    favorite_color_str = input("Enter favorite color (Red/Green/Yellow/Blue): ")

    gender = Gender[gender_str]
    marital_status = MaritalStatus[marital_status_str]
    favorite_color = Color[favorite_color_str]

    address = Address(street_name, building_no, po_box, zip_code)
    contact_info = ContactInfo(phone, email, address)
    person = Person(first_name, last_name, contact_info, gender, marital_status, favorite_color)

    return person

# Read person information from the user
person1 = read_person_info()

# Print the street name
print(person1.contact_info.address.street_name)

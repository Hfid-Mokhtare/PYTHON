import re

def validate_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def validate_phone_number(phone_number):
    phone_pattern = r"^(\+?)(?:[0-9] ?){6,14}[0-9]$" 
    phone_pattern = r"^((\+212)|0)[5-7][0-9]{8}$"
    return re.match(phone_pattern, phone_number) is not None

def validate_ip_adress(ip):
    ip_pattern = r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
    return re.match(ip_pattern, ip) is not None

# Example usage
email1 = "valid_email@example.com"
email2 = "invalid_email"

phone = "+123456789012345"
phone1 = "+1 (555) 555-1234"
phone2 = "555-1234"
phone3 = "abc-123-4567"

ip="122.255.1.1"

if validate_email(email1):
    print(f"{email1} is a valid email address.")
else:
    print(f"{email1} is not a valid email address.")

if validate_email(email2):
    print(f"{email2} is a valid email address.")
else:
    print(f"{email2} is not a valid email address.")
#----------------------------------------------------------
if validate_phone_number(phone):
    print(f"{phone} is a valid phone number.")
else:
    print(f"{phone} is not a valid phone number.")

if validate_phone_number(phone2):
    print(f"{phone2} is a valid phone number.")
else:
    print(f"{phone2} is not a valid phone number.")

if validate_phone_number(phone3):
    print(f"{phone3} is a valid phone number.")
else:
    print(f"{phone3} is not a valid phone number.")
#----------------------------------------------------------


if validate_ip_adress(ip):
    print(f"{ip} is a valid ip")
else:
    print(f"{ip} is not a valid ip")
    

import re

import re


# re.match -------------------------------------------
text = "This is a string to match."

    # Match the entire string (pattern starts at the beginning)
match = re.match(r"This is a string", text)

if match:
    print("Match found at the beginning:", match.group())
else:
    print("No match at the beginning")

# re.search -------------------------------------------
    
text = "This has a match in the middle."

    # Find the pattern anywhere in the string
match = re.search(r"match", text)

if match:
    print("Match found anywhere:", match.group())
else:
    print("No match found")
    
# re.findall -------------------------------------------
    
text = "Red, Green, Blue, Red"

# Find all occurrences of colors
colors = re.findall(r"\w+", text)  # \w+ matches one or more word characters

print("All color matches:", colors)

# re.sub -------------------------------------------

text = "AAABBBCCC"

# Replace all occurrences of 'A' or 'C' with 'X' (case-insensitive)
new_text = re.sub(r"[AC]", "X", text, flags=re.IGNORECASE)

print("Substituted string:", new_text)

# re.compile -------------------------------------------

pattern = re.compile(r"\d+")  # Compiled pattern for digits

text = "My phone number is 123-456-7890."

    # Use the compiled pattern for searching (more efficient than repeated re.search)
match = pattern.search(text)

if match:
    print("Found phone number:", match.group())
else:
    print("No phone number found")
    
# re.split -------------------------------------------
    
text = "This is, a comma, separated string."

    # Split the string using commas
split_text = re.split(r",", text)

print("Split string:", split_text)

# re.fullmatch -------------------------------------------

text = "Complete match"

    # Full match requires the entire string to match
match = re.fullmatch(r"Complete match", text)

if match:
    print("Full match found:", match.group())
else:
    print("No full match found")
# Example -------------------------------------------
logs = """
User 1: 192.168.1.1 - accessed at 10:45 AM
User 2: 10.0.0.5 - accessed at 10:50 AM
User 3: Invalid IP: 999.999.999.999
User 4: 172.16.254.1 - accessed at 11:00 AM
User 5: 255.255.255.255 - Admin Login
User 6: 0.0.0.0 - Test Server
"""

pattern=r"(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"
# r"(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"
match=re.findall(pattern, logs)
if match:
    print(match)
else: 
    print("not matching")




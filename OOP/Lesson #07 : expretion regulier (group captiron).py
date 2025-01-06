
import re
motif_data = re.compile(r"(\d\d) (\w+) (\d{4})")
corresp = motif_data.search(" Tanger le 08 janvier 2025")
print("corresp.group() : ", corresp.group())
print("corresp.group(1) : ", corresp.group(1))
print("corresp.group(2) : ", corresp.group(2))
print("corresp.group(3) : ", corresp.group(3))
print("corresp.group(1,3) : ", corresp.group(1,3))
print("corresp.group() : ", corresp.groups())

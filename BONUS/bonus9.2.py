password = input("Enter new password:")
result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False
digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digit"] = digit

upperCase = False
for i in password:
    if i.isdigit():
        upperCase = True
result["upperCase"] = upperCase
print(result)
if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")

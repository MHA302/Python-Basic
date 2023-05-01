password = input("Enter a new Password:")
result = {}
if len(password) > 7:
    print("Great Password There!")
elif len(password) == 7:
    print("Password is OK, but not too strong")
else:
    print("Your Password is weak!")
password = input("Enter a password")


def strength(password):
    result = {}
    if len(password) > 8:
        result['password'] = True
    else:
        result['password'] = False

    digit = False
    uppercase = False
    for i in password:
        if i.isdigit():
            digit = True
        if i.isupper():
            uppercase = True
        result['digits'] = digit
        result['upper-case'] = uppercase

    if all(result.values()):
        return 'Strong Password'
    else:
        return "Weak password"


print(strength(password))




country =[]
while True:
    user_action = input("Enter your Country Name:")
    user_action = user_action.strip()
    match user_action:
        case 'USA' | 'usa':
            print("Hello WELCOME to USA")
        case 'Pakistan' | 'pakistan':
            print("Assalam-u-alaikum........")
        case 'Germany' | 'germany':
            print('Hallo.....')
        case _:
            print('Please Enter a valid Country Name')
print("GOOD BYE")

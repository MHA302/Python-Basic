try:
    width = float(input("Enter the recatangle width:"))
    length = float(input('Enter The rectangle length:'))
    if width == length:
        exit("That Look Like A Square ")
    area = width * length
    print(area)
except ValueError:
    print("Please Enter a Number")
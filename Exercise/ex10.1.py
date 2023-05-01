try:
    total_value = int(input("Enter total value:"))
    value = int(input('Enter value:'))
    if total_value == 0:
        print("Your Total value cannot be zero")
    else:
        percentage = value / total_value * 100
        print(f"That is: {percentage} %")
except ValueError:
    print(" You need to  Enter a Number.Run the program a again")
cubic_liter = input("Enter the number of liters:")


def convert_liters(cubic_liter):
    liters = float(cubic_liter)
    cub_liter = liters * 1000
    return cub_liter


print(convert_liters(cubic_liter))
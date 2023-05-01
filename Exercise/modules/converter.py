def convert(temp,high_temp=90, low_temp=0):
    if low_temp <= temp <= high_temp:
        return "Liquid"
    elif temp <= low_temp:
        return "Solid"
    elif temp >= high_temp:
        return "Gas"
    else:
        return "Please Enter a Valid Temp"


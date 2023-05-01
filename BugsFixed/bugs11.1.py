def get_maximum():
    celsius = [14, 15.1, 12.3]
    high = max(celsius)
    print("Temp in Degree C:", high)
    return high


high = get_maximum()

fahrenheit = high * 1.8 + 32
print("Temp in Degree Fahrenheit:", fahrenheit)
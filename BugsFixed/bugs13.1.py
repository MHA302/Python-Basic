def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


h = float(input("Enter value of height:"))
time = calculate_time(h, g=9.80665)
print(time)

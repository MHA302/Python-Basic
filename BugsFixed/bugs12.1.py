distance = input("Enter distance:")
time = input("Enter time:")


def speed(distance, time):
    distance = float(distance)
    time = float(time)
    v = distance / time
    return v


print(speed(distance, time))

while True:
    with open("sides.txt", 'r') as file:
        sides = file.readlines()

    side = input("THrow the coin  and enter head and tail:") + "\n"

    sides.append(side)

    with open("sides.txt", 'w') as file:
        file.writelines(sides)

    num_of_heads = sides.count("head\n")
    percentage = num_of_heads / len(sides) * 100
    print(f"Heads :{percentage}%")
temperatures = [10, 12, 14]
temperatures = [str(i) + '\n 'for i in temperatures]
file = open("../files/file.txt", 'w')

file.writelines(temperatures)

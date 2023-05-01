filenames = ['a.txt', 'b.txt', 'c.txt']
for filename in filenames:
    file = open(f"../files/{filename}", 'r')
    data = file.read()
    file.close()
    print(data)

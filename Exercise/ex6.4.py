filenames = ["doc.txt", "report.txt", "presentation.txt"]
for file in filenames:
    file = open(f"../files/{file}", 'w')
    file.write("Hello")
    file.close()

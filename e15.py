import glob

files = glob.glob("file/*.txt")

for filepath in files:
    with open(filepath, 'r') as file:
        print(file.read()) 
contents = ["All carrots are to be sliced longitudinally.",
            "The Carrots were reportedly sliced.",
            "The Slicing process was well presented. "]

filenames = ["doc.txt",
             "report.txt",
             "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.writelines(content)


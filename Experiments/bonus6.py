contents = ["All carroot are to be sliced","I came to office ","you go for walk"]
filenames = ["doc.txt","report.txt","presentation.txt"]

for content, filename in zip(contents,filenames):
    file = open(f"files/{filename}","w")
    file.write(content)
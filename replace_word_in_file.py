with open("file1.txt","r") as file1:
    contents=file1.read()
    contents=contents.replace("hello","how")

with open("file1.txt","w") as file1:
    file1.write(contents)   
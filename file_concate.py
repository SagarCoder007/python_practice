
with open("file1.txt","r") as file1 ,open("file2.txt","r")as file2:
    contents=file1.read()+"\n"+file2.read()

with open("merged.txt","w") as merge_file:
    merge_file.write(contents)    
word_to_count="hello"
with open("file1.txt") as file1:
    contents=file1.read()
    count=contents.count(word_to_count)
    print(f"the word {word_to_count} appears {count} in a file")
    

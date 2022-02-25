def wordCount():
    count=0
    file=open("C98.txt")
    lines=file.readlines()
    print(lines)
    for i in lines:
        words=i.split()
        count=count+len(words)
    print(count)
    print(len(lines))

wordCount()

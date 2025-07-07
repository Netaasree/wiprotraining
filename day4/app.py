with open("File.txt",'a+') as file:
    file.write('\n Append data')
    file.seek(0)
    print(file.read())
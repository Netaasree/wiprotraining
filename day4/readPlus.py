with open('File.txt','w+') as file:
    content=file.read()
    file.seek(0)
    file.write("       here")
try:
    file=open('sample.csv')
    str=file.readline()
    str2=file.readline()
    print(str)
    print(str2)
except IOError:
    print("Error occured during input take.....")
else:
    print("Successfully feteched the data......")
    
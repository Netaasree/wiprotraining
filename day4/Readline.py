# with open("File1.txt",'r') as file:
#     lines=file.readlines()
# print("List of lines",lines)






# with open("File1.txt",'r') as file:
#     lines=file.readlines()

# for line in lines:
#     print(line.strip())


# with open("File1.txt",'r') as file:
#     separate_lines = [line.strip() for line in file.readline()]
#     print(separate_lines)



# file = open("File1.txt",'r')
# print(file.closed)
# file.close()
# print(file.closed) # type: ignore


"""program to create a txt file access the text file data and use
data to split the lines into series of words and use space to perform
split operation
sample.txt
Hello students
How are you today
o/p:["Hello","students","how","are","you","today"]
"""
#program:
with open("sample.txt","r") as file:
    #liness = [line.strip() for line in file.readline()]
    lis=[]
    for line in file.readline():
        x=line.strip()
        lis.append(x)
    print(lis)
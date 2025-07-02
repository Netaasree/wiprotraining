import itertools
data=input("Enter characters: ")
permute=list(itertools.permutations(data))
print("All permutations")
for p in permute:
    with open("people",'w') as file:
        print(' '.join(p))

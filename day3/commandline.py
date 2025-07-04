import sys
if len(sys.argv)<2:
    print("usage:python hi.py <name>")
else:
    name=sys.argv[1]
    print(f"Student, {name},{sys.argv}!")
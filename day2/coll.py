from collections import Counter
text = input("Enter a text: ")
counter = Counter(text)
print(dict(counter))
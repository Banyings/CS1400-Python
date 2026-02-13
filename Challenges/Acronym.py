# Welcome to Acronym Generator
print("Welcome to Acronym Generator")
sentence = ""
while sentence != "q":
    sentence = input("Enter a sentence or q to quit: ")
    pos = 0
    acronym = sentence[0]
    while pos >= 0 and sentence != "q":
        pos = sentence.find(" ", pos)
        if pos >= 0:
            pos += 1
            acronym += sentence[pos]
    if sentence != "q":
        print("Acronym:", acronym.upper())

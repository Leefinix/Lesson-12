string = input("Enter you're own a word: ")
char = input("Enter you're own a letter: ")

i = 0 
count = 0

while (i < len(string)):
    if (string[i] == char):
        count += 1
    i += 1

print("The total number of times ", char, "has occured is: ", count)
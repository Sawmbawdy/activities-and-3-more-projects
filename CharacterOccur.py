Word = str(input("Type the word you want to scan: \n"))
char = str(input("Type the character you want to find: \n"))
count = 0   
i = 0
while i < len(Word):
    if Word[i] == char:
        count += 1
    i += 1
    
print("The character", char, "appears", count, "times in the word", Word)
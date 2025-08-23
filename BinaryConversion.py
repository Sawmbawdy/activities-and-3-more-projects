num = float(input("Enter a decimal number: \n"))
binary = bin(int(num)).replace("0b", "")
print("The binary representation of", float(num), "is", binary)
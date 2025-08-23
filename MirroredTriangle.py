Rows = int(input("Enter the number of rows: \n"))
t = Rows
space = Rows - 1
stars = 1

for i in range(Rows, 0, -1):
    for j in range(1, t):
        print(space * " ",stars * "*", stars * "*", sep='')
        space -= 1
        stars += 1
        break
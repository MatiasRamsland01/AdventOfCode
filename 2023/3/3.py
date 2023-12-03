values = []
matrix = []
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
with open("input.txt", "r") as textfile:
    for line in (textfile):
        array = []
        for char in line.strip():
            array.append(char)
        matrix.append(array)

currentPart = ""
valid = False
for i, x in enumerate(matrix):
    if (currentPart != "" and valid):
        values.append(int(currentPart)) 
    currentPart = ""
    valid = False
    for j, y in enumerate(x):
        #Checks current position. If . go next
        if (matrix[i][j] == "." or matrix[i][j] not in numbers):
            if (currentPart != "" and valid):
                values.append(int(currentPart)) 
            currentPart = ""
            valid = False
            continue
        currentPart += y
        for di, dj in neighbors:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]):
                if matrix[ni][nj] != '.' and matrix[ni][nj] not in numbers:
                    valid = True
                    break  # Exit loop if a valid neighbor is found
       
        


# print(matrix)
print(sum(values))


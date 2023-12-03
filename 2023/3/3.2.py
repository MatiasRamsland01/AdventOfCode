from typing import Dict, List

# Type hint indicating keys are strings and values are lists
gears: Dict[str, List[int]] = {}
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
gearPos = ""
for i, x in enumerate(matrix):
    if (currentPart != "" and valid and gearPos != ""):
        if (gearPos in gears):
            gears[gearPos].append(int(currentPart))
        else:
            gears[gearPos] = [int(currentPart)]
    currentPart = ""
    valid = False
    gearPos = ""
    for j, y in enumerate(x):
        #Checks current position. If . go next
        if (matrix[i][j] == "." or matrix[i][j] not in numbers):
            if (currentPart != "" and valid and gearPos != ""):
                if (gearPos in gears):
                    gears[gearPos].append(int(currentPart))
                else:
                    gears[gearPos] = [int(currentPart)]
            currentPart = ""
            valid = False
            gearPos = ""
            continue
        currentPart += y
        for di, dj in neighbors:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]):
                if matrix[ni][nj] == '*':
                    valid = True
                    gearPos = str(ni)+str(nj)
                    break  # Exit loop if a valid neighbor is found
       
        


# print(matrix)
print(sum(value[0] * value[1] for value in gears.values() if len(value) == 2))




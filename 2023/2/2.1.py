import math
values = []
colors = ["red", "green", "blue"]
def game_possible(input : str) -> int:
    minValues = {"red": 0, "green": 0, "blue": 0}
    for set in input.split(";"):
        for cubes in set.split(","):
            for color in colors:
                if color in cubes:
                    value = int(cubes.replace(color, ''))
                    break
            else:
                continue  # Skip if no color matches

            # if (color == "red" and value > 12) or \
            #    (color == "green" and value > 13) or \
            #    (color == "blue" and value > 14):
            #     return 0
            if (minValues[color] < value):
                minValues[color] = value
    return math.prod(list(minValues.values()))
with open("input.txt", "r") as textfile:
    for i, line in enumerate(textfile):
        gameString = line[line.find(":")+1::].replace(" ", "").strip()

        values.append(game_possible(gameString))
       
print(sum(values))


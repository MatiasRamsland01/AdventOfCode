values = []
colors = ["red", "green", "blue"]
def game_possible(input : str) -> bool:
    for set in input.split(";"):
        for cubes in set.split(","):
            for color in colors:
                if color in cubes:
                    value = int(cubes.replace(color, ''))
                    break
            else:
                continue  # Skip if no color matches

            if (color == "red" and value > 12) or \
               (color == "green" and value > 13) or \
               (color == "blue" and value > 14):
                return False
    return True
with open("input.txt", "r") as textfile:
    for i, line in enumerate(textfile):
        gameString = line[line.find(":")+1::].replace(" ", "").strip()

        if (game_possible(gameString)):
            values.append(i+1)
       
print(sum(values))


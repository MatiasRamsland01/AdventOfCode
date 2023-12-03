values = []
with open("input.txt", "r") as textfile:
    for line in textfile:
        lineValue = []
        line_stripped = line.strip()
        for value in line_stripped:
            try:
                valueInt = int(value)
                lineValue.append(value)
            except:
                pass
        values.append(int((lineValue[0]+lineValue[-1])))

print(sum(values))

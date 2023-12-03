string_values = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
def replace_number_words(input_str : str) -> str:
    input_str = input_str.strip()
    for word, digit in string_values.items():
        index = input_str.find(word)
        while index != -1:
            index = input_str.find(word)
            if (index != -1):
                listStr = list(input_str)
                listStr.insert(index + 1, digit)
                input_str = ''.join(listStr)
            index = input_str.find(word)
    return input_str



values = []
with open("input.txt", "r") as textfile:
    for line in textfile:
        lineValue = []
        line = replace_number_words(line)
        line_stripped = line.strip()
        for value in line_stripped:
            try:
                valueInt = int(value)
                lineValue.append(value)
            except:
                pass
        print(lineValue)
        values.append(int((lineValue[0]+lineValue[-1])))

print(sum(values))
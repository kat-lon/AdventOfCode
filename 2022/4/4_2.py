def get_pair_values(line):
    line.strip("\n")
    pairs = line.split(",")
    stringvalues = [value.split("-") for value in pairs]
    values = []

    for stringList in stringvalues:
        values.append((int(stringList[0]), int(stringList[1])))

    return values

def compare_values(values):
    if ((values[0][0] in range(values[1][0], values[1][1]+1))
    or (values[0][1] in range(values[1][0], values[1][1]+1))
    or (values[1][0] in range(values[0][0], values[0][1]+1))
    or (values[1][1] in range(values[0][0], values[0][1]+1))):
        return 1
    else:
        return 0

    

with open("adventOfCode/2022/4/pairs.txt") as file:
    lines = file.readlines()

count = 0
for line in lines:
        count += compare_values(get_pair_values(line))

print(count)
def find_repeated_item(line):
    item = ""
    for c in line:
        if (c in line[len(line)//2:]):
            item = c
            break

    return item

def get_item_value(item):
    value = ord(item) - 96
    if (value < 0):
        value += 58
    return value


with open("adventOfCode/2022/3/storage.txt") as file:
    lines = file.readlines()

result = 0
for line in lines:
    result += get_item_value(find_repeated_item(line))
print(result)

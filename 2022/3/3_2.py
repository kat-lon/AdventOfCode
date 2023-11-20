def find_repeated_item(group):
    item = ""
    for c in group[0]:
        if (c in group[1] and c in group[2]):
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
for group in range(2, len(lines), 3):
    result += get_item_value(find_repeated_item(lines[:3]))
    lines = lines[3:]
print(result)
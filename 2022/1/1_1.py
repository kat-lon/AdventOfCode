def elf_inventory(lines):
    inventory = [0]
    i = 0;
    for line in lines:
        if (len(line) > 1):
            inventory[i] += int(line)
        else:
            i += 1
            inventory.append(0)

    return inventory

def find_max_calories(inventory):
    maxcal = -1
    for food in inventory:
        if (food > maxcal):
            maxcal = food

    return maxcal

    
with open("adventOfCode/2022/1/inventory.txt") as file:
    lines = file.readlines()

inventory = elf_inventory(lines)
print(find_max_calories(inventory))
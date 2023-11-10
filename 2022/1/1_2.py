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
    maxcal = [-1,-1,-1]
    for food in inventory:
        if (food > maxcal[0]):
            if (food > maxcal[1]):
                if (food > maxcal[2]):
                    maxcal[0] = maxcal[1]
                    maxcal[1] = maxcal[2]
                    maxcal[2] = food
                    continue
                maxcal[0] = maxcal[1]
                maxcal[1] = food
                continue
            maxcal[0] = food
            
    return maxcal

    
with open("adventOfCode/2022/1/inventory.txt") as file:
    lines = file.readlines()

inventory = elf_inventory(lines)
maxcal = find_max_calories(inventory)
total = 0
for i in maxcal:
    total += i

print(total)
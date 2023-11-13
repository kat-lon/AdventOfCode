def get_pair_values(line):
    line.strip("\n")
    pairs = line.split(",")
    return [value.split("-") for value in pairs]
    

  

with open("adventOfCode/2022/4/pairs.txt") as file:
    lines = file.readlines()

count = 0
for line in lines:
    values = get_pair_values(line)
    if ((int(values[0][0]) <= int(values[1][0]) 
    and int(values[0][1]) >= int(values[1][1]))
    or (int(values[1][0]) <= int(values[0][0]) 
    and int(values[1][1]) >= int(values[0][1]))):
        count += 1

print(count)
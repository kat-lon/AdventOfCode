key_iterations = [i*20 for i in range(1, 12, 2)]
key_values = []
iteration = 0
X = 1

def addx(n):
    global X
    save_key_values()
    X += n
    save_key_values()

def save_key_values():
    global iteration, X
    iteration += 1
    if (iteration in key_iterations): key_values.append(X)

def console(lines):
    for line in lines:
        line = line.split()
        if line[0] == "addx":
            addx(int(line[1]))
        else:
            save_key_values()

def count_frecuency_value():
    global key_values, key_iterations
    n = 0
    for v, i in zip(key_values, key_iterations):
        n += i * v
    return n

with open("adventOfCode/2022/10/cpu.txt") as file:
    lines = file.readlines()

save_key_values()
console(lines)

print(count_frecuency_value())



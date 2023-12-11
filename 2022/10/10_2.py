iteration = 0
X = 1

def addx(n):
    global X
    cicle()
    cicle()
    X += n

def cicle():
    global iteration, X
    print(f"{"#" if iteration in range(X-1, X+2) else "."}", end="")
    iteration += 1
    if (iteration == 40): 
        iteration = 0
        print()

def console(lines):
    for line in lines:
        line = line.split()
        if line[0] == "addx":
            addx(int(line[1]))
        else:
            cicle()

with open("adventOfCode/2022/10/cpu.txt") as file:
    lines = file.readlines()

console(lines)
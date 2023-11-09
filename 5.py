def createStorage(line):
    storage = []
    i = 1
    while(i < len(line)-1):
        storage.append([])
        i += 4
    return storage

def fillCrates(lines):
    crates = createStorage(lines[0])
    finalLine = 0

    for line in lines:
        
        if(line[1].isdigit()):
            finalLine += 2
            break

        i, j = 1, 0
        while(i < (len(line) - 1)):
            if(line[i] != " "):
                crates[j].append(line[i])
            i += 4
            j += 1

        finalLine += 1

    for stack in crates:
        stack.reverse()
        
    return crates, finalLine

def getMoves(lines):
    moves = []
    for line in lines:
        words = line.split()
        moves.append((int(words[1]), int(words[3]), int(words[5])))

    return moves

def moveCrates(moves, crates):

    for move in moves:
        i = 0
        while(i < move[0]):
            crates[move[2]-1].append(crates[move[1]-1].pop())
            i += 1

    return crates


with open("2022/2022-5/crates.txt") as file:
    lines = file.readlines()

crates, startingLine = fillCrates(lines)
moves = getMoves(lines[startingLine:])
crates = moveCrates(moves,crates)
for stack in crates:
    print(stack.pop())

def create_storage(line):
    storage = []
    i = 1
    while(i < len(line)-1):
        storage.append([])
        i += 4
    return storage

def fill_crates(lines):
    crates = create_storage(lines[0])
    final_line = 0

    for line in lines:
        
        if(line[1].isdigit()):
            final_line += 2
            break

        i, j = 1, 0
        while(i < (len(line) - 1)):
            if(line[i] != " "):
                crates[j].append(line[i])
            i += 4
            j += 1

        final_line += 1

    for stack in crates:
        stack.reverse()
        
    return crates, final_line

def get_moves(lines):
    moves = []
    for line in lines:
        words = line.split()
        moves.append((int(words[1]), int(words[3]), int(words[5])))

    return moves

def move_crates(moves, crates):

    for move in moves:
        i = 0
        while(i < move[0]):
            crates[move[2]-1].append(crates[move[1]-1].pop())
            i += 1

    return crates


with open("adventOfCode/2022/5/crates.txt") as file:
    lines = file.readlines()

crates, startingLine = fill_crates(lines)
moves = get_moves(lines[startingLine:])
crates = move_crates(moves,crates)
result = ""
for stack in crates:
    result += stack.pop()
print(result)
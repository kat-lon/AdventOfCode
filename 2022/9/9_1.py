directions = {"U": (1, 0), "D": (-1, 0), "L": (0, -1), "R": (0, 1)}

def move_head(head_pos, direction):
    movement = directions[direction]
    head_pos[0] += movement[0]
    head_pos[1] += movement[1]

def move_tail(head_pos, tail_pos):
    distance = [head_pos[i] - tail_pos[i] for i in range(0, 2)]

    if (0 in distance and (2 in distance or -2 in distance)):
        for i in range(0, 2):
            if (distance[i] not in range(-1, 2)):
                tail_pos[i] += 1 if distance[i] > 0 and distance[i] not in range(-1, 2) else -1    
    elif (2 in distance or -2 in distance):
        for i in range(0, 2):           
            tail_pos[i] += 1 if distance[i] > 0 else -1
        


def execute_moves(moves):
    head_pos, tail_pos, final_pos, all_tail_pos = [0,0], [0,0], [0,0], [[0,0]]
    for move in moves:
        instructions = move.split()
        for _ in range(int(instructions[1])):
            move_head(head_pos, instructions[0])
            move_tail(head_pos, tail_pos)
            for _ in range():
                move_tail(tail_pos, final_pos)

            if (tail_pos not in all_tail_pos):
                all_tail_pos.append(tail_pos[:])

    return all_tail_pos
            

with open("adventOfCode/2022/9/moves.txt") as file:
    lines = file.readlines()

print(len(execute_moves(lines)))

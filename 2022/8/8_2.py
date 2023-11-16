compass = {"north": (-1, 0), "south": (1, 0), "east": (0, 1), "west": (0, -1)}

def create_matrix(lines):
    matrix = []
    for line in lines:
        matrix.append([])
        for c in line:
            if (c != "\n"):
                matrix[len(matrix)-1].append(int(c))

    return matrix

def get_scenic_score(tree_coordinates, forest):
    tree_height = forest[tree_coordinates[0]][tree_coordinates[1]]
    scenic_score = 1

    for cardinal_point in compass:
        current_position = tree_coordinates[:]
        cardinal_score = 0

        while (0 not in current_position and len(forest) - 1 not in current_position):
            cardinal_score += 1
            current_position[0] += compass[cardinal_point][0]
            current_position[1] += compass[cardinal_point][1]
            if (forest[current_position[0]][current_position[1]] >= tree_height):
                break
        
        scenic_score *= cardinal_score

    return scenic_score

def highest_scenic_score(forest):
    high_score = 0

    for line_position in range(1, len(forest) -1):
        tree_line = forest[line_position]

        for tree_position in range(1, len(tree_line)-1):
            score = get_scenic_score([line_position, tree_position], forest)
            high_score = score if score > high_score else high_score
        

    return high_score


with open("adventOfCode/2022/8/forest.txt") as file:
    lines = file.readlines()

print(highest_scenic_score(create_matrix(lines)))

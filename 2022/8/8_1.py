compass = {"north": (-1, 0), "south": (1, 0), "east": (0, 1), "west": (0, -1)}

def create_matrix(lines):
    matrix = []
    for line in lines:
        matrix.append([])
        for c in line:
            if (c != "\n"):
                matrix[len(matrix)-1].append(int(c))

    return matrix

def is_visible_tree(tree_coordinates, forest):
    tree_height = forest[tree_coordinates[0]][tree_coordinates[1]]

    for cardinal_point in compass:
        is_visible = True
        current_position = tree_coordinates[:]

        while (0 not in current_position and len(forest) - 1 not in current_position and is_visible):
            current_position[0] += compass[cardinal_point][0]
            current_position[1] += compass[cardinal_point][1]
            is_visible = forest[current_position[0]][current_position[1]] < tree_height

        if(is_visible):
            break

    return is_visible

def count_visible_trees(forest):
    visible_trees = len(forest)*2 + len(forest[0])*2 - 4
    for line_position in range(1, len(forest) -1):
        tree_line = forest[line_position]
        for tree_position in range(1, len(tree_line)-1):
            if (is_visible_tree([line_position, tree_position], forest)):
                visible_trees += 1

    return visible_trees


with open("adventOfCode/2022/8/forest.txt") as file:
    lines = file.readlines()

print(count_visible_trees(create_matrix(lines)))


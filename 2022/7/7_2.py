from directory import Directory

root = Directory(None, "root")

def execute_cd(current_dir, new_dir):
    if (new_dir == ".."):
        current_dir = current_dir.father
    else:
        current_dir = current_dir.get_child(new_dir)
    
    return current_dir


def get_best_dir(starting_dir, best_option, min_size):
    for child in starting_dir.children:
        best_option = get_best_dir(child, best_option, min_size)
    if (starting_dir.size > min_size and starting_dir.size < best_option):
        return starting_dir.size
    return best_option

def run_commands(commands, current_dir):
    for command in commands:
        command = command.split()

        if (command[0] == "$" and command[1] == "cd"):
            current_dir = execute_cd(current_dir, command[2])
            continue

        if (command[0] == "dir"):
            current_dir.add_child(Directory(current_dir, command[1]))
            continue

        if (command[0].isdigit()):
            current_dir.increment_size(int(command[0]))
    
    
with open("adventOfCode/2022/7/comands.txt") as file:
    lines = file.readlines()

run_commands(lines[1:], root)
print(get_best_dir(root, 70_000_000, 30_000_000 - (70_000_000 - root.size) ))
from directory import Directory

root = Directory(None, "root")

def execute_cd(current_dir, new_dir):
    if (new_dir == ".."):
        current_dir = current_dir.father
    else:
        current_dir = current_dir.get_child(new_dir)
    
    return current_dir

#Recursividad??? si
def get_children_sizes(starting_dir):
    size = 0
    for child in starting_dir.children:
        size += get_children_sizes(child)
    return size if starting_dir.size > 100_000 else size + starting_dir.size
    
with open("adventOfCode/2022/7/comands.txt") as file:
    lines = file.readlines()
lines = lines[1:] #Vaya parche mas feo
current_dir = root
for command in lines:
    command = command.split()

    if (command[0] == "$" and command[1] == "cd"):
        current_dir = execute_cd(current_dir, command[2])
        continue

    if (command[0] == "dir"):
        current_dir.add_child(Directory(current_dir, command[1]))
        continue

    if (command[0].isdigit()):
        current_dir.increment_size(int(command[0]))


print(get_children_sizes(root))

    
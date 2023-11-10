plays = {"A":-1, "B":-2, "C":-3, "X":1, "Y":2, "Z":3}

def rock_paper_scissors(lines):

    points = 0
    for line in lines:
        result = plays[line[0]] + plays[line[2]]
        points += plays[line[2]]
        if (result == 0):
            points += 3
        elif (result == 1 or result == -2):
            points += 6

    return points

        

with open("adventOfCode/2022/2/strategy.txt") as file:
    lines = file.readlines()

print(rock_paper_scissors(lines))


plays = {"AX":3, "AY":4, "AZ":8, "BX":1, "BY":5, "BZ":9, "CX":2, "CY":6, "CZ":7}

def rock_paper_scissors(lines):

    points = 0
    for line in lines:
        points += plays[f"{line[0]}{line[2]}"]

    return points

        

with open("adventOfCode/2022/2/strategy.txt") as file:
    lines = file.readlines()

print(rock_paper_scissors(lines))
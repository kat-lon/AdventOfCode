def find_marker(stream):
    marker = 4
    marker_found = False
    for i in range(0, len(stream) - 4):
        for j in range(0, 4):
            if (stream[i + j] in stream[i + j + 1:i+4]):
                break
            else:
                marker_found = j == 3
        if(marker_found):
            break
        marker += 1
    return marker


with open("adventOfCode/2022/6/datastream.txt") as file:
    lines = file.readlines()
print(find_marker(lines[0]))
    
def find_marker(stream, marker_length):
    marker = marker_length
    marker_found = False
    for i in range(0, len(stream) - marker_length):
        for j in range(0, marker_length):
            if (stream[i + j] in stream[i + j + 1:i + marker_length]):
                break
            else:
                marker_found = j == marker_length - 1
        if(marker_found):
            break
        marker += 1
    return marker


with open("adventOfCode/2022/6/datastream.txt") as file:
    lines = file.readlines()
print(find_marker(lines[0], 14))
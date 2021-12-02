# Advent of code Puzzle input reader.
# The following code assumes that your puzzle input exists in a
# file called data.txt, one entry per line

with open('data.txt', 'r') as f:
    lines = f.readlines()
puzzle_input = [e.strip() for e in lines]


horizontal_position = 0
depth = 0
for input in puzzle_input:
    # print(f"{input}") # TEST CODE
    string_list = input.split()
    # print(string_list) # TEST CODE
    if string_list[0] == "forward":
        horizontal_position += int(string_list[1])
    if string_list[0] == "up":
        depth -= int(string_list[1])
    if string_list[0] == "down":
        depth += int(string_list[1])

print(horizontal_position)
print(depth)

print(f"multplay is: {horizontal_position * depth}")

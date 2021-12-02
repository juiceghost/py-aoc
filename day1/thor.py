# Advent of code Puzzle input reader.
# The following code assumes that your puzzle input exists in a
# file called data.txt, one entry per line

with open('data.txt', 'r') as f:
    lines = f.readlines()
puzzle_input = [int(e.strip()) for e in lines]

count = 0
for num, input in enumerate(puzzle_input[1:], start=1):
    print(f"{num}: {input}")
    if input > puzzle_input[num-1]:
        count += 1
        print(count)
print(f"count is: {count}")

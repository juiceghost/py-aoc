with open('data.txt', 'r') as f:
    lines = f.readlines()
puzzle_input = [e.strip() for e in lines]

up = 0
down = 0
forward = 0
for line in puzzle_input:
    if line[0] == 'u':
        up -= int(line[-1])
    elif line[0] == 'd':
        down += int(line[-1])
    elif line[0] == 'f':
        forward += int(line[-1])
    else:
        print('Something happened')

depth = up+down
pos = depth*forward
print(pos)

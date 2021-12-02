with open('data.txt', 'r') as f:
    lines = f.readlines()
puzzle_input = [e.strip() for e in lines]

#print(puzzle_input[3].split(" "))
data = dict()
route = []
for item in puzzle_input:
    foo = item.split(" ")
    data[foo[0]] = foo[1]
    route.append(data)
    data = dict()

# loopa igenom datan
depth = 0
position = 0
# forward X ökar position med X
# down X ökar djupet med X
# up X minskar djupet med X

# GLÖM INTE ATT MULTIPLICERA depth och position i slutet!!!!
for change in route:
    # tolka key i change
    key = list(change.keys())[0]
    # print(key[0])
    value = int(list(change.values())[0])
    # print(value[0])
    if key == 'up':
        depth -= value
    if key == 'down':
        depth += value
    if key == 'forward':
        position += value

print(depth * position)

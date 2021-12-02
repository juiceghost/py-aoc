with open('data.txt', 'r') as f:
    lines = f.readlines()
puzzle_input = [int(e.strip()) for e in lines]

count = 0
for index, item in enumerate(puzzle_input):
    try:
        if item < puzzle_input[index+3]:
            count += 1
    except:
        print(index)
print(count)

amount = 0
for index, item in enumerate(puzzle_input):
    try:
        a = item+puzzle_input[index+1]+puzzle_input[index+2]
        b = puzzle_input[index+1]+puzzle_input[index+2]+puzzle_input[index+3]
        if a < b:
            amount += 1
    except:
        print(index)
print(amount)

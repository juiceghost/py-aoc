# Advent of code Puzzle input reader.
# The following code assumes that your puzzle input exists in a
# file called data.txt, one entry per line

with open('data.txt', 'r') as f:
    lines = f.readlines()
puzzle_input = [int(e.strip()) for e in lines]

count = 0
# print(puzzle_input[1999])
""" for index, item in enumerate(puzzle_input[1:], start=1):
    print(f'index: {index} item: {item}')
    input("pause") """
# print(puzzle_input[-2])

""" 
for index, item in enumerate(puzzle_input):
    # print(f'index: {index} item: {item}')
    # för varje element i listan
    # jämför med föregående element
    # om nuvarande djup är högre än föregående öka count med 1
    if index > 0:
        if item > puzzle_input[index - 1]:
            count += 1
print(count)
 """

# loopa igenom listan
# ta aktuellt item, plussa på nästa och nästnästa item
# spara denna summa (three-measurement window) i en ny lista
sums = []
for index, item in enumerate(puzzle_input):
    if index < len(puzzle_input) - 2:
        sums.append(item + puzzle_input[index + 1] + puzzle_input[index + 2])

for index, item in enumerate(sums):
    # print(f'index: {index} item: {item}')
    # för varje element i listan
    # jämför med föregående element
    # om nuvarande djup är högre än föregående öka count med 1
    if index > 0:
        if item > sums[index - 1]:
            count += 1
print(count)

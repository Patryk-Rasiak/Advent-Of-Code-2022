from collections import defaultdict

with open("05/5a.txt") as f:
    data, commands = f.read().split("\n\n")

data = data.replace('[', '').replace(']', '').split("\n")[:-1]
commands = commands.split("\n")
stacks = defaultdict(lambda: [])

# Extracting data to dictionary - each stack to each key - value pair
for line in data:
    line = line.replace('    ', ' ').split(' ')
    for i, val in enumerate(line):
        if val.strip():
            stacks[i+1].append(val)
        else:
            stacks[i+1] = []

# Iterating over commands
for command in commands:
    command = command.split()
    quantity, move_from, move_to = int(command[1]), int(command[3]), int(command[5])

    # Putting items on top of desired stack
    stacks[move_to] = list(reversed(stacks[move_from][:quantity])) + stacks[move_to]
    
    # Removing those items from previous stack
    stacks[move_from] = stacks[move_from][quantity:]

# Extracting first element from each stack to get the result
result = ''
for values in stacks.values():
    if values:
        result += values[0]

print(result)
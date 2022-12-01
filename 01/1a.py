with open("01/1a.txt") as f:
    data = f.read().split("\n\n")

max_value = 0
for line in data:
    current_sum = sum([int(x) for x in line.split("\n")])
    if current_sum > max_value:
        max_value = current_sum
print(max_value)


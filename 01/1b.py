with open("01/1b.txt") as f:
    data = f.read().split("\n\n")

top1 = top2 = top3 = 0
for line in data:
    current_sum = sum([int(x) for x in line.split("\n")])
    if current_sum > top1:
        top3, top2, top1 = top2, top1, current_sum
    elif current_sum > top2:
        top3, top2 = top2, current_sum
    elif current_sum > top3:
        top3 = current_sum

print(sum([top1, top2, top3]))

    
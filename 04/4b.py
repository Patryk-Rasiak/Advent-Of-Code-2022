with open("04/4a.txt") as f:
    data = f.readlines()

counter = 0
for line in data:
    first, second = line.split(",")

    first1, first2 = map(int, first.split("-"))
    second1, second2 = map(int, second.split("-"))

    first_interval = set(range(first1, first2 + 1))
    second_interval = set(range(second1, second2 + 1))

    if len(first_interval.intersection(second_interval)) > 0:
        counter += 1

print(counter)

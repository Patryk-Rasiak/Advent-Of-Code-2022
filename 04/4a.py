with open("04/4a.txt") as f:
    data = f.readlines()

counter = 0
for line in data:
    first, second = line.split(",")

    first1, first2 = map(int, first.split("-"))
    second1, second2 = map(int, second.split("-"))

    if (first1 <= second1 and first2 >= second2) or (first1 >= second1 and first2 <= second2):
        counter += 1

print(counter)

with open("02/2a.txt") as f:
    data = f.read().splitlines()

points_for_outcome = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6
}

print(sum(points_for_outcome[line] for line in data))
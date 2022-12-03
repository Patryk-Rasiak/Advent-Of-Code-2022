with open("03/3a.txt") as f:
    data = f.read().splitlines()

alphabet = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = 0
for i in range(0, len(data), 3):
    common = set.intersection(set(data[i]), set(data[i+1]), set(data[i+2])).pop()
    result += alphabet.index(common)
print(result)
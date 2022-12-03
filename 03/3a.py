with open("03/3a.txt") as f:
    data = f.read().splitlines()

alphabet = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = 0
for line in data:
    first, second = set(line[:len(line)//2]), set(line[len(line)//2:])
    common = first.intersection(second).pop()
    result += alphabet.index(common)
print(result)  
    
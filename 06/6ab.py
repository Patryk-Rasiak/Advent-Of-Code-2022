with open("06/6a.txt") as f:
    data = f.read().strip()

def signal_device(num_distinct_characters):
    for i in range(len(data)-num_distinct_characters):
        sequence = data[i:i+num_distinct_characters]
        if len(sequence) == len(set(sequence)):
            return i+num_distinct_characters


# 6a
print(signal_device(4))

# 6b
print(signal_device(14))

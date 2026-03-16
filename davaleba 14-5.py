words = ["apple", "banana", "avocado", "blueberry", "cherry"]

grouped = {}

for w in words:
    first = w[0]

    if first not in grouped:
        grouped[first] = []

    grouped[first].append(w)

print(grouped)
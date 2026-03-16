nums = [2, 5, 6, 2, 8, 9, 6, 10, 3, 8]

evens = []

for x in nums:
    if x % 2 == 0 and x not in evens:
        evens.append(x)

print(evens)
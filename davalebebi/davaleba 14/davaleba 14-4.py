scores = {
    "Giorgi": 88,
    "Nino": 95,
    "Luka": 82,
    "Ana": 91,
    "Dato": 87
}

sorted_students = sorted(scores.items(),
                         key=lambda x: x[1],
                         reverse=True)

top3 = sorted_students[:3]

for name, score in top3:
    print(name, score)
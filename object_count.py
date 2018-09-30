objects = [1, 2, 3, 3, 3, 'Hello', {'4'}, 0]

scores = set()
for i in objects:
    idObject = id(i)
    if not (idObject in scores):
        scores.add(idObject)

print(len(scores))

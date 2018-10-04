from collections import deque


def bfs(g, start):
    queue, enqueued = deque([(None, start)]), set([start])
    while queue:
        parent, n = queue.popleft()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        queue.extend([(n, child) for child in new])


def shortest_path(g, start, end):
    paths = {None: []}
    for parent, child in bfs(g, start):
        paths[child] = paths[parent] + [child]
        if child == end:
            return paths[child]
    return None


# поиск в ширину был найден на сайте аннимона
classes = {}
n = int(input())
for i in range(n):
    tmp = input()
    tmp = tmp.replace(":", " ").split()
    #    print(tmp)
    classes[tmp[0]] = [] if len(tmp) == 1 else tmp[1:]
homeless = []
for i in classes.values():
    for j in i:
        if j not in classes.keys():
            homeless.append(j)
for i in homeless: classes[i] = []
fullclasses = []
for i in classes.items():
    fullclasses.append(i[0])
    for j in i[1]:
        fullclasses.append(j)
# print(classes)
# print(fullclasses)
n = int(input())
for i in range(n):
    l, r = input().split()
    if l == r:
        print("Yes")
    elif l not in fullclasses or r not in fullclasses:
        print("No")
    elif shortest_path(classes, r, l) == None:
        print("No")
    else:
        print("Yes")

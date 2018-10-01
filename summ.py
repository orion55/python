count = int(input())
list = []

for i in range(count):
    list.append(int(input()))

sum = 0
for i in list:
    sum += i

print(sum)

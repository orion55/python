def count_str(s, t):
    count = 0
    res = 0

    while True:
        res = s.find(t, res)
        if res != -1:
            count += 1
            res += 1
        else:
            break

    return count


s = str(input())
t = str(input())
print(count_str(s, t))
# s = "abababa"
# t = "aba"
# print(count_str(s, t))
# s = "aaaaa"
# t = "a"
# print(count_str(s, t))
# s = "abc"
# t = "abc"
# print(count_str(s, t))
# s = "abababa"
# t = "abc"
# print(count_str(s, t))

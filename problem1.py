def foo(s, a, b):
    answer = 0
    while a in s:
        prev = s
        s = s.replace(a, b)
        if (prev in s) or (a in b):
            answer = "Impossible"
            break
        answer += 1
    print(answer)


s = str(input())
a = str(input())
b = str(input())
foo(s, a, b)
# print("Test #1")
# foo("ababa", "a", "b")
# print("Test #2")
# foo("ababa", "b", "a")
# print("Test #3")
# foo("ababa", "c", "c")
# print("Test #4")
# foo("ababac", "c", "c")
# print("Test #5")
# foo("abababa", "aba", "ada")
# print("Test #6")
# foo("aabbcc", "aa", "aaa")
# print("Test #7")
# foo("abbb", "ab", "a")
# print("Test #8")
# foo("abbb", "ab", "aabc")

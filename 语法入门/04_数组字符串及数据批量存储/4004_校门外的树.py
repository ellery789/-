l, m = map(int, input().split())
removed = [False] * (l + 1)
for _ in range(m):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        removed[i] = True
print(removed.count(False))

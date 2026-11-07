n, x = map(int, input().split())
print(sum(str(i).count(str(x)) for i in range(1, n + 1)))

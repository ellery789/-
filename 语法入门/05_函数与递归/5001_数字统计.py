l, r = map(int, input().split())
print(sum(str(i).count("2") for i in range(l, r + 1)))

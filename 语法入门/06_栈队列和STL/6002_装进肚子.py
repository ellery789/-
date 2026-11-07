n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

gain = sorted((a[i] - b[i] for i in range(n)), reverse=True)
print(sum(b) + sum(gain[:k]))

import sys

data = sys.stdin.read().split()
t = int(data[0])
out = []
for k in range(1, t + 1):
    n = int(data[k])
    for i in range(1, n + 1, 2):
        out.append(" " * ((n - i) // 2) + "*" * i)
    for i in range(n - 2, 0, -2):
        out.append(" " * ((n - i) // 2) + "*" * i)
print("\n".join(out))

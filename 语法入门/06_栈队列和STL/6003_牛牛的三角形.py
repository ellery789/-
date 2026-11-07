import sys

data = sys.stdin.read().split()
n = int(data[0])
a = sorted(map(int, data[1:1 + n]), reverse=True)

ans = None
for i in range(n - 2):
    if a[i + 1] + a[i + 2] > a[i]:
        ans = (a[i], a[i + 1], a[i + 2])
        break

print("No solution" if ans is None else " ".join(map(str, sorted(ans))))

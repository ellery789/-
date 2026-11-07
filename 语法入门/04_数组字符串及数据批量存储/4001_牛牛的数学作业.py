import sys

data = sys.stdin.read().split()
pos = 0
t = int(data[pos]); pos += 1
out = []
for _ in range(t):
    n = int(data[pos]); pos += 1
    a = list(map(int, data[pos:pos + n])); pos += n
    s = sum(a)
    sq = sum(x * x for x in a)
    rng = max(a) - min(a)

    var = (n * sq - s * s) / (n * n)
    out.append(f"{rng} {var:.3f}")
print("\n".join(out))

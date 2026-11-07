import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)

    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    for i in range(1, n + 1):
        print(" " * 2 * (n - i + 1) + "*" * i)
    print("*" * (n + 1))
    for j in range(1, n + 1):
        print(" " * 2 * j + "*" * (n + 1 - j))

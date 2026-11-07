import sys


def is_leap(y: int) -> bool:
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for line in sys.stdin:
    parts = line.split()
    if len(parts) < 3:
        continue
    y, m, x = map(int, parts)
    days = DAYS[m - 1]
    if m == 2 and is_leap(y):
        days = 29
    target = str(x)
    total = 0
    for d in range(1, days + 1):
        date = f"{y:04d}-{m:02d}-{d:02d}"
        total += date.count(target)
    print(total)

n = int(input())
num = 1
for i in range(1, n + 1):
    row = []
    for _ in range(i):
        row.append(f"{num:4d}")
        num += 1
    print("".join(row))

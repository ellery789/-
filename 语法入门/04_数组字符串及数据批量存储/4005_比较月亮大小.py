n = int(input())
a = list(map(int, input().split()))

if n == 1:
    if a[0] == 0:
        print("UP")
    elif a[0] == 15:
        print("DOWN")
    else:
        print("-1")
else:
    prev, last = a[-2], a[-1]
    if last > prev:
        print("DOWN" if last == 15 else "UP")
    else:
        print("UP" if last == 0 else "DOWN")

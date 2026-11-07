c = input().strip()
levels = ord(c) - ord("A")

for i in range(levels + 1):
    left = " " * (levels - i)
    up = "".join(chr(ord("A") + k) for k in range(i + 1))
    down = up[-2::-1] if i > 0 else ""
    print(left + up + down)

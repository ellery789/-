counts = list(map(int, input().split()))
odd = [d for d in range(10) if counts[d] % 2 == 1]

if len(odd) > 1:
    print(-1)
elif not any(counts[d] for d in range(1, 10)):

    print(0 if counts[0] == 1 else -1)
else:
    half = []
    for d in range(10):
        half += [str(d)] * (counts[d] // 2)
    half.sort()
    if half and half[0] == "0":
        nz = [k for k, ch in enumerate(half) if ch != "0"]
        if not nz:

            print(-1)
        else:
            half[0], half[nz[0]] = half[nz[0]], half[0]
            left = "".join(half)
            mid = str(odd[0]) if odd else ""
            print(left + mid + left[::-1])
    else:
        left = "".join(half)
        mid = str(odd[0]) if odd else ""
        print(left + mid + left[::-1])

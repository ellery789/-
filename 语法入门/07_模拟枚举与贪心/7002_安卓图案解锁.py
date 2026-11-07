import sys


MID = {
    frozenset((1, 3)): 2, frozenset((4, 6)): 5, frozenset((7, 9)): 8,
    frozenset((1, 7)): 4, frozenset((2, 8)): 5, frozenset((3, 9)): 6,
    frozenset((1, 9)): 5, frozenset((3, 7)): 5,
}

for line in sys.stdin:
    s = line.strip()
    if not s:
        continue
    used = set()
    prev = None
    ok = True
    for ch in s:
        d = int(ch)
        if d in used:
            ok = False
            break
        if prev is not None:
            mid = MID.get(frozenset((prev, d)))
            if mid is not None and mid not in used:
                ok = False
                break
        used.add(d)
        prev = d
    print("YES" if ok else "NO")

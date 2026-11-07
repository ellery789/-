results = []
digits = "123456789"

for a in range(2, 5000):
    for b in range(a, 10000 // a + 1):
        c = a * b
        s = str(a) + str(b) + str(c)
        if len(s) == 9 and "".join(sorted(s)) == digits:
            results.append((c, a, b))

results.sort()
for c, a, b in results:
    print(f"{c} = {a} x {b}")

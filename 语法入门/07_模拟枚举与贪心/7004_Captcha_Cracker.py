import sys

words = {"zero": "0", "two": "2", "four": "4", "six": "6", "nine": "9"}
digits = {"0": "0", "2": "2", "4": "4", "6": "6", "9": "9"}

data = sys.stdin.read().split()
t = int(data[0])
out = []
for k in range(1, t + 1):
    s = data[k]
    res = []
    i = 0
    while i < len(s):
        if s[i] in digits:
            res.append(digits[s[i]])
            i += 1
            continue
        for w, d in words.items():
            if s.startswith(w, i):
                res.append(d)
                i += len(w)
                break
        else:
            i += 1
    out.append("".join(res))
print("\n".join(out))

import sys

data = sys.stdin.read().split()
n, t = int(data[0]), int(data[1])
int_part, _, dec = data[2].partition(".")

while t > 0:

    idx = next((i for i, ch in enumerate(dec) if ch >= "5"), None)
    if idx is None:
        break
    t -= 1

    digits = int_part + dec[:idx]
    lst = list(digits)
    j = len(lst) - 1
    while j >= 0 and lst[j] == "9":
        lst[j] = "0"
        j -= 1
    if j >= 0:
        lst[j] = str(int(lst[j]) + 1)
        total = "".join(lst)
    else:
        total = "1" + "0" * len(lst)
    if idx > 0:
        int_part, dec = total[:-idx], total[-idx:]
    else:
        int_part, dec = total, ""

dec = dec.rstrip("0")
print(f"{int_part}.{dec}" if dec else int_part)

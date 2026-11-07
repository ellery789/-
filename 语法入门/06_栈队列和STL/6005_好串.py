import sys

s = sys.stdin.readline().strip()
stack = []
ok = True
for ch in s:
    if ch == "b" and stack and stack[-1] == "a":
        stack.pop()
    else:
        stack.append(ch)

print("Good" if not stack else "Bad")

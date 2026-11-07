import sys

s = sys.stdin.read()
out = []
i = 0
state = 0
com_start = 0
while i < len(s):
    if state == 0:
        if s.startswith("/*", i):
            state = 2
            com_start = i
            i += 2
        elif s[i] == '"':
            state = 1
            out.append(s[i])
            i += 1
        else:
            out.append(s[i])
            i += 1
    elif state == 1:
        if s[i] == "\\":
            out.append(s[i:i + 2])
            i += 2
        elif s[i] == '"':
            state = 0
            out.append(s[i])
            i += 1
        else:
            out.append(s[i])
            i += 1
    else:
        if s.startswith("*/", i):
            state = 0
            i += 2
        else:
            i += 1

if state == 2:
    out.append(s[com_start:])
sys.stdout.write("".join(out))

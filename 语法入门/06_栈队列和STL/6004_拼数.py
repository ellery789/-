from functools import cmp_to_key

n = int(input())
nums = input().split()


def compare(x: str, y: str) -> int:
    return -1 if x + y > y + x else (1 if x + y < y + x else 0)


print("".join(sorted(nums, key=cmp_to_key(compare))))

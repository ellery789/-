x, y = map(int, input().split())


def digit_sum(n: int) -> int:
    return sum(int(ch) for ch in str(n))


print(sum(1 for i in range(min(x, y), max(x, y) + 1) if digit_sum(i) % 5 == 0))

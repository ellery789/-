t = input().strip()
s = t + t[-2::-1]
num = int(s)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


print("prime" if is_prime(num) else "noprime")

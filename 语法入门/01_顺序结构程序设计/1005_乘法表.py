for i in range(1, 10):
    items = [f"{j}*{i}={i * j:2d}" for j in range(1, i + 1)]
    print(" ".join(items))

def digitalSum(n):
    if n < 10:
        return n
    else:
        x = digitalSum(n // 10)
        n %= 10
        x += n
        return x

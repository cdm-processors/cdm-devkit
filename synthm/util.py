def log2(k):
    res = 0
    x = 1  # x=2**res, invariant
    while x < k:
        res += 1
        x = x * 2
    # x>=k, res>=log(k)
    return res

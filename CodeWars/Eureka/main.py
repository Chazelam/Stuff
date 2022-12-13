def calc(x):
    n = 0
    out = 0
    x = str(x)
    while (len(x)>n):
        num = int(x[n])
        out += num**(n + 1)
        n += 1
    return out

def sum_dig_pow(a, b): 
    res = []
    for i in range(a, b + 1):
        if calc(i) == i:
            res.append(i)
    return res
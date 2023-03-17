def sum_n(k, n):
    Sum = 0
    while k < n:
        Sum = Sum + s(k)
        k += 1
    return Sum

def s(k):
    return (2**k)*(a(k)**2 - b(k)**2)

def a(k):
    if k == 0:
        return 1
    else: 
        return (a(k-1)+b(k-1))/2

def b(k):
    if k == 0:
        return 1/(2**0.5)
    else:
        return (a(k-1)*b(k-1))**0.5

def U(x):
    return (2*(a(x+1)**2))/(1 - sum_n(0, x))

n = int(input("n: ")) + 1
print("Pi: ", U(n))
input("Press enter to exit ")
# Consider the number 1176 and its square (1176 * 1176) = 1382976. Notice that:

# the first two digits of 1176 form a prime.
# the first two digits of the square 1382976 also form a prime.
# the last two digits of 1176 and 1382976 are the same.

# Given two numbers representing a range (a, b), how many numbers satisfy this property within that range? (a <= n < b)

#Example
#solve(2, 1200) = 1, 
#because only 1176 satisfies this property within the range 2 <= n < 1200. 
# See test cases for more examples. The upper bound for the range will not exceed 1,000,000.

def prime(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2*i, len(sieve), i):
                sieve[j] = 0
    sieve = list(set(sieve))
    sieve.remove(0)
    return sieve

def solve(a,b):
    count = 0
    primes = prime(100)
    for num in range(a, b+1):
        numSqr = num**2
        firstTwoNum = int(str(num)[:2])
        firstTwoSqr = int(str(numSqr)[:2])
        if (firstTwoNum in primes) and (firstTwoSqr in primes) and num % 100 == numSqr % 100:
            count += 1
    return count

print(solve(1, 10000))
def factors(n):
    list = []
    for i in range(1, n + 1):
        if n % i == 0:
            list = list + [i]
    return list

def isprime(n):
    return(factors(n) == [1, n])

z = isprime(1)
print(z)

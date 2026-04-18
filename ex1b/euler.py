def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def mod_pow(base, exp, mod):
    result = 1
    for _ in range(exp):
        result = (result * base) % mod
    return result

def prime_factors(n):
    factors = set()
    temp = n

    while temp % 2 == 0:
        factors.add(2)
        temp //= 2

    i = 3
    while i * i <= temp:
        while temp % i == 0:
            factors.add(i)
            temp //= i
        i += 2

    if temp > 2:
        factors.add(temp)

    return factors

def euler_totient():
    n = int(input("Enter n: "))
    a = int(input("Enter a (for Fermat test): "))

    print("\n--- EULER TOTIENT THEOREM ---")
    print("Given n =", n)

    print("\nStep 1: Fermat Test")
    val = mod_pow(a, n-1, n)
    print(a, "^", (n-1), "mod", n, "=", val)

    if val == 1:
        print("=> n is PROBABLY PRIME")
        print("phi(", n, ") =", n-1)
        return

    print("=> n is COMPOSITE")

    print("\nStep 2: Prime Factorization")
    factors = prime_factors(n)
    print("Prime factors:", factors)

    print("\nStep 3: Apply Formula")
    print("phi(n) = n * (1 - 1/p1) * (1 - 1/p2) ...")

    phi = n
    for p in factors:
        print("Multiply by (1 - 1/", p, ")", sep="")
        phi *= (1 - 1/p)

    print("\nphi(", n, ") =", int(phi))

euler_totient()

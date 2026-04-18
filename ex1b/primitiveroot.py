
def mod_pow(base, exp, mod):
    result = 1
    for _ in range(exp):
        result = (result * base) % mod
    return result


def primitive_root():
    p = int(input("Enter prime number p: "))

    if p <= 1:
        print("Invalid input: Enter prime number > 1")
        return

    print("\n--- PRIMITIVE ROOT CHECK ---")
    print("For p =", p)
    print("Check a^i mod p for i = 1 to", p-1)

    roots = []

    for g in range(2, p):
        print("\nChecking a =", g)

        values = set()

        for i in range(1, p):
            val = mod_pow(g, i, p)
            values.add(val)

            print(g, "^", i, "mod", p, "=", val)

        print("Unique values count =", len(values))

        if len(values) == p - 1:
            print("=>", g, "is a PRIMITIVE ROOT")
            roots.append(g)
        else:
            print("=>", g, "is NOT a primitive root")

    print("\nPrimitive Roots:", roots)

primitive_root()

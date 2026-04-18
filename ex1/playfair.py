def generate_matrix(key):
    key = key.upper().replace("J", "I")
    used = []

    for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in used:
            used.append(c)

    return used

def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = ''.join(c for c in text if c.isalpha())

    res = ""
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"

        if a == b:
            res += a + "X"
            i += 1
        else:
            res += a + b
            i += 2

    return res

def playfair_rule(a, b, matrix, direction):
    p1, p2 = matrix.index(a), matrix.index(b)
    r1, c1 = divmod(p1, 5)
    r2, c2 = divmod(p2, 5)

    if r1 == r2:
        return matrix[r1*5+(c1+direction)%5] + matrix[r2*5+(c2+direction)%5]
    elif c1 == c2:
        return matrix[((r1+direction)%5)*5+c1] + matrix[((r2+direction)%5)*5+c2]
    else:
        return matrix[r1*5+c2] + matrix[r2*5+c1]

def playfair_cipher(text, key, mode):
    matrix = generate_matrix(key)

    print("\n--- MATRIX ---")
    for i in range(0,25,5):
        print(matrix[i:i+5])

    if mode == "encrypt":
        text = prepare_text(text)
        print("\n--- BIGRAMS ---")
        pairs = [text[i:i+2] for i in range(0,len(text),2)]
        print(pairs)

        print("\n--- ENCRYPTION ---")
        result = ""
        for p in pairs:
            c = playfair_rule(p[0], p[1], matrix, 1)
            print(p, "->", c)
            result += c

    else:
        text = ''.join(c for c in text.upper() if c.isalpha())
        print("\n--- DECRYPTION ---")
        result = ""
        for i in range(0,len(text),2):
            pair = text[i:i+2]
            p = playfair_rule(pair[0], pair[1], matrix, -1)
            print(pair, "->", p)
            result += p

    print("\nResult:", result)

text = input("Enter text: ")
key = input("Enter key: ")
mode = input("Encrypt or Decrypt: ").lower()

playfair_cipher(text, key, mode)

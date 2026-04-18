def shift_cipher(text, key, mode):
    text = ''.join(c for c in text.upper() if c.isalpha())

    if key < 0 or key > 25:
        print("Invalid key")
        return

    if mode == "decrypt":
        key = 26 - key

    print("\n--- SHIFT CIPHER ---")

    result = ""
    for ch in text:
        p = ord(ch) - 65
        c = (p + key) % 26

        print(ch, "->", p, "-> (", p, "+", key, ") mod 26 =", c, "->", chr(c+65))
        result += chr(c + 65)

    print("\nResult:", result)

text = input("Enter text: ")
key = int(input("Enter key (0-25): "))
mode = input("Encrypt or Decrypt: ").lower()

shift_cipher(text, key, mode)

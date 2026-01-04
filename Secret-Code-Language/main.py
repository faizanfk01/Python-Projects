import random

code_decode = input("Do you want to code or decode?: ").lower()
alphabets = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+=-"

if code_decode == "code":
    code = input("Enter a sentence or word to code: ").lower()
    words = code.split()
    coded_words = []

    for word in words:
        if len(word) >= 3:
            prefix = ''.join(random.choices(alphabets, k=3))
            suffix = ''.join(random.choices(alphabets, k=3))
            modified = word[1:] + word[0]
            coded_words.append(prefix + modified + suffix)
        else:
            coded_words.append(word[::-1])

    coded = " ".join(coded_words)
    print(f"Coded: {coded}")

elif code_decode == "decode":
    decode = input("Enter the coded sentence or word to decode: ").lower()
    words = [w.strip() for w in decode.split() if w.strip()]
    decoded_words = []

    for word in words:
        if len(word) > 6:
            trimmed = word[3:-3]
            if trimmed:
                decoded = trimmed[-1] + trimmed[:-1]
            else:
                decoded = ""
            decoded_words.append(decoded)
        else:
            decoded_words.append(word[::-1])

    decoded = " ".join(decoded_words)
    print(f"Decoded: {decoded}")

else:
    print("Invalid Input!")
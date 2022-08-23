veta = input("veta: ")

# pro každý znak v proměnné veta
for c in veta:

    # pokud je to A, E, I, O U
    if c in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        print("", end="")
    # pokud ne, napiš znak
    else:
        print(c, end="")
print(" ")

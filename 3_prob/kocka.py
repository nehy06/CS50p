def main():
    pocet = get_number()
    meow(pocet)


def get_number():
    while True:
        n = int(input("Kolikrát má kočka zamňoukat? "))
        if n > 0:
            break
    return n


def meow(p):
    for _ in range(p):
        print("meow")


main()

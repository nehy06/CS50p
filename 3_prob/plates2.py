from curses.ascii import isdigit


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # ověření, zda má vstup délku 2 <= plate < 7
    if len(s) < 2 or len(s) > 6:
        return False
    # kontrola, zda 1 nebo druhé místo neobsahují číslo
    elif s[0].isdigit() or s[1].isdigit():
        return False
    # v s jsou pouze čísla a písmena
    elif s.isalnum() == False:
        return False

    # kontrola, za se ve stringu někde nachází 0
    for i in range(len(s)):  # V ROZSAHU délky stringu s
        if s[i].isdigit():  # je znak v s na pozici i číslo
            if int(s[i]) == 0:  # pokud se toto číslo rovná 0, false
                return False
            elif not (s[i+1::].isalpha()) == False:
                return False
            # pokud po 0 uporostřed následuje písmeno, false
        elif s[i].isdigit() and s[i + 1].isalpha():
            return False
            # (s[i+1::]).isalpha() == False:  # na pozici i + 1 je písmeno
        else:
            return True


main()

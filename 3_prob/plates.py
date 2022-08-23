from curses.ascii import isalpha


def main():
    plate = input("Plate: ")
    if lenght(plate) == True and first_two(plate) == True and punct(plate) == True no_num_middle(plate) == True:
        print("Valid")
    else:
        print("Invalid")


# fce co kontroluje délku
def lenght(plate):
    if 2 <= len(plate) < 7:
        return True
    else:
        return False


# funkce co kontroluje první dva znaky
def first_two(plate):
    for char in plate:
        if plate[0:2].isalpha():
            return True
        else:
            return False


# žádné tečky, čárky atp.
def punct(plate):
    for char in plate:
        if char.isalnum():
            return True
        else:
            return False

# první číslo nesmí být 0, musí končit číslem, ne písmenem


def no_num_middle(plate):
    if

# žádné číslo uprostřed, jen na konci - rozodit si plate na seznam znaků? pokud na 1 a druhém místě písmeno, valid, pokud ne invalid


main()

# ptej se uživatele na vstup, dokud to neukončí ctrl - d
# potom zobraz všechny položky, které uživatel zadal, velkými písmeny, seřazený podle abecedy, před nimi číslo, kolikrát uživatel danou věc zadal - když zadá jablko 2X, výstup bude  - 2 jablko

list = {}

while True:
    try:
        # vyžadám si vstup
        item = input("")
        item = item.upper().strip()
        # do list přidám položku získou v proměnné item, navýším jí o 1,
        list[item] = list.get(item, 0) + 1

# pokud to uživatel ukončí ctrl d, break ze smičky while true
    except EOFError:

        # zalomím řádek z promt
        print("\n")

        # na internetu nalezený, jak podle abecedy seřadit dict - dict jméno je list, vytvořím nový s názven sorted_list = fce co někdo udělal :-D
        sorted_list = dict(sorted(list.items(), key=lambda x: x[0].lower()))
        for item in sorted_list:
            print(sorted_list[item], item)
        break

camel_case = input("camelCase: ")

# pro každý znak v proměnné camel_case
for c in camel_case:

    # pokud je to malé písmeno, jen ho vypiš a nezalamuj řádek
    if c.islower():
        print(c, end="")
    # pokud ne, napiš _ a přidej zmíněnné písmeno, ale malé
    else:
        print("_" + c.lower(), end="")
print(" ")

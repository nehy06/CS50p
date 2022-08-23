zbyva = 50

while zbyva > 0:

    print("Amount due :", zbyva)
    mince = int(input("insert coin: "))

    if mince in [5, 10, 25]:
        zbyva = zbyva - mince


change_owed = abs(zbyva)
print("change owned: ", change_owed)

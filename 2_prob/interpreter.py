# vstup od uživatele
vyraz = input("Zadej matematicky vyraz: ")

# rozdělení vstupu
x, y, z = vyraz.split(" ")

# výpočet
if y == "+":
    reseni = float(x) + float(z)
elif y == "-":
    reseni = float(x) - float(z)
elif y == "*":
    reseni = float(x) * float(z)
else:
    reseni = float(x) / float(z)

print(round(reseni, 1))

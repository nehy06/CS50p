# TEST CASES
# - enter taco, enter taco again == $6.00
# - enter baja taco, enter tortilla salad == $12.00
# - enter burger > reprompt user

from functools import total_ordering


menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# stanovím si pořáteční cenu, která je u každé objednávky 0 :)

total_price = 0
# neustále se chci ptát na vstup a ověřovat podmínky a počtíta cenu
while True:
    try:

        # vyždádání vstupu + velké první písmeno, jinak nedojde k match
        order = input("Item: ")
        order = order.title()

        # pro každou položku v listu menu
        for x in menu:

            # jestliže hodnota proměnné order se shoduje s aktuálně kontrolovanou položkou v listu (x)
            if order == x:
                total_price = total_price + menu[x]
                print("Total: $" + str(total_price) + "0")
            # pokud ne, di dál
            else:
                continue

    except EOFError:
        print("\n")
        break

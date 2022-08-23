from decimal import DivisionByZero
from xml.dom.minidom import Element

while True:
    # vstup
    x = input("zlomek: ")
    try:
        # rozdělit vstup a převést na int
        citatel, jmenovatel = x.split("/")
        int_citatel = int(citatel)
        int_jmenovatel = int(jmenovatel)
        # výpočet %
        fuel_perc = int_citatel / int_jmenovatel
        # ověřit <1, zastavit smyčku
        if fuel_perc <= 1:
            break
    except (ValueError):
        print("ValueError")
        pass
    except (ZeroDivisionError):
        print("ZeroDivisionError")
        pass

if fuel_perc <= 0.01:
    print("E")
elif fuel_perc >= 0.99:
    print("F")
else:
    perc = int(round(fuel_perc * 100))
    print(f"{perc}%")

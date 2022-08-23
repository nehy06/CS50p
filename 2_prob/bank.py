pozdrav = input("Jak pozdravíš? ")

prefix1 = "hello"
prefix2 = "h"

if pozdrav.lower().startswith(prefix1):
    print("0$")
elif pozdrav.lower().startswith(prefix2):
    print("20$")
else:
    print("100$")

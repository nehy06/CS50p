x = input(
    "What is the answer to hte Great Question of Life, the Universe, and Everything? ")

if x.lower().strip() == "42" or x.lower().strip() == "forty-two" or x.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")

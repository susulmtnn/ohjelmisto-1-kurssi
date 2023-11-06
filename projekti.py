import copy

icecreams = {
    "vanilla": 1,
    "strawberry": 2,
    "blueberry": 3,
    "truffle": {"milk": 4,
             "coconut": 5,},
}

dessert = icecreams.copy()
print(dessert)
dessert["truffle"]["milk"]=69
copieddessert= copy.deepcopy(dessert)
print(dessert)
print(icecreams)

for flavour, num in icecreams.items():
    if flavour == "vanilla":
        print(num)

print("(m$^3$/s)")

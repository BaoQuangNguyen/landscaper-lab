money = 0

tools = {
    "teeth": 1,
}

while True:
    cut = input("What tool would you like to cut grass with today? (teeth) ")

    if cut == "quit":
        break

    if cut in tools:
        money += tools[cut]
        print(f"You cut grass with {cut} and earned ${tools[cut]}! You currently have ${money} ")
    else:
        print("Not a tool!")



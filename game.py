money = 0

tools = {
    "teeth": 1,
}

buy_tools = {
    "rusty scissors": 5,
}

while True:
    print(f"You currently have ${money}. Your available tools: {', '.join(tools.keys())}")
    
    cut = input("What tool would you like to cut grass with today? ")

    if cut.lower() == "quit":
        break

    if cut in tools:
        money += tools[cut]
        print(f"You cut grass with {cut} and earned ${tools[cut]}! ")

        if money >= 5 and "rusty scissors" not in tools.keys():
            print("rusty scissors is available for purchase! ")

    elif cut == "buy":
        buy = input("What tool would you like to buy? (rusty scissors) ")
        if buy in buy_tools:
            price = buy_tools[buy]
            if money >= price:
                if buy not in tools.keys():
                    money -= price
                    tools[buy] = buy_tools[buy]
                    print(f"You bought {buy} for ${price}! ")
                else:
                    print("You already  have that tool!")
            else:
                print("Not enough money!")
        else:
            print("Not a valid tool!")
    else:
        print("Not a tool!")

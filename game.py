money = 0

tools = {
    "teeth": 1,
}

buy_tools = {
    "rusty scissors": 5,
    "push lawnmower": 25,
    
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
        elif money >= 25 and "push lawnmower" not in tools.keys():
            print("push lawnmower is available for purchase! ")
        
    elif cut == "buy":
        print("Available tools for purchase:")
        for tool, price in buy_tools.items():
            print(f"{tool} (${price})")
        buy = input("Enter the name of the tool you would like to buy: ")
        
        if buy in buy_tools:
            price = buy_tools[buy]
            if money >= price:
                if buy not in tools.keys():
                    money -= price
                    if buy == "push lawnmower":
                        tools[buy] = 50
                    else:
                        tools[buy] = buy_tools[buy]
                    print(f"You bought {buy} for ${price}! ")
                    del buy_tools[buy]
            else:
                print("Not enough money!")
        else:
            print("Not a valid tool!")
    else:
        print("Not a tool!")

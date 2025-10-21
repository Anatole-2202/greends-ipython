
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


price=0
while True: #The loop allows to keep asking user to input again and again
    try:
        item=input("Item: ")
        item=item.title() #titlecasing input to match with the menu
        price+=float(menu[item]) #Sum of the prices
        print(f"${price:.2f}")
    except KeyError:
        continue
        #the except KeyError allows to continue aking user even if the name of the dish is wrong
    except EOFError: #CTRL-D
        print('\n')
        break #ctrl-d induces E0FError and the end of the loop, with '\n' to move user cursor at the last line of terminal

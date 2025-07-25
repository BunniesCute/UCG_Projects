
#funtion for the menu

order = []

print("="*50)
print("Welcome to the digital restrant!")
print("="*50)
def menu():
    
    print("\nMENU↓")
    print("\nMain:")
    print("\n1.Spaghetti - $10.99")
    print("\n2.Chesseburgers - $10.50")
    print("\n3.Hot pot - $20.50")

    print("\nSides:")
    print("\n1.Fries")
    print("\n2.Fruit Cup")
    print("\n3.Potato Salad")

    print("\nDrinks:")
    print("\n1.Lemonade")
    print("\n2.Soda")
    print("\n3.Root Beer float")
    print("\n4.Water")
    print("="*50)


menu()

Main_dish1 = "Spaghetti"
Main_dish2 = "Chesseburger"
Main_dish3 = "Hot pot"

Side1 = "Fries"
Side2 = "Fruit Cup"
Side3 = "Potato Salad"

Drink1 = "Lemonade"
Drink2 = "Soda"
Drink3 = "Root Beer Float"
Drink4 = "Water"

price1 = 10.99
price2 = 10.50
price3 = 20.50 



order1 = input("Enter your main (1-3): ")
   
    
order2 = input("Enter a side(1-3): ")

order3 = input("Enter a drink(1-4): ")





if order1 == "1":
    order.append(Main_dish1)
elif order1 == "2":
    order.append(Main_dish2)
elif order1 == "3":
    order.append(Main_dish3)
else:
    print("That is not a main")


if order2 == "1":
    order.append(Side1)
elif order2 == "2":
     order.append(Side2)
elif order2 == "3":
    order.append(Side3)
else:
    print("Thats not a side")
            

if order3 == "1":
    order.append(Drink1)
    print(f"{order}")
elif order3 == "2":
     order.append(Drink2)
     print(f"{order}")
elif order3 == "3":
     order.append(Drink3)
     print(f"{order}")
elif order3 == "4":
    order.append(Drink4)
    print(f"{order}")
else:
    print("Thats not a drink.")
            

if order1 == "1":
    print(f"Your bill is ${price1}")
elif order1 == "2":
    print(f"Your bill is ${price2}0")
elif order1 == "3":
    print(f"Your bill is ${price3}0")
else:
    print("That item is not on my menu.")
        

print("\nGoodbye!\n")

print("="*50)
raise





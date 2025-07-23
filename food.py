
#Making the starting list
food = ["Pizza", "Tacos", "Burgers", "Sushi", "Fries"]
print("Starting food list", food)

#Adding a new item to the list
new_food = input("Enter one food to add to the list: ")
food.append(new_food)
print("Added! New list: ",food)

#removing an item from a list
remove_food = input("Enter a food you want to remove from the list: ")
if remove_food in food:
    food.remove(remove_food)
    print(f"Removed {remove_food}")
else:
    print(f"⚠️ {remove_food} is not in the list.")
print("Current list:",len(food))

#sorting the list
sort = input("Do you want to sort alphabtically? yes/no: ").lower()
if sort == "yes":
    food.sort()
    print("Sorted list:", food)
else:
    print("Skipping sort...")
    print(food)
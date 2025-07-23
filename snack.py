

snacks = []
count = 0

while count < 3:
    snack = input(f"Enter snack #{count + 1}: ")
    snacks.append(snack)
    count += 1

print("\n Your fav snacks are:", snacks)

snacks.sort()
print("Sorted snacks: ", snacks)
remove = input("\nRemove a snack: ")

if remove in snacks:
    snacks.remove(remove)
    print("Removed snack:",remove)
else:
    print("⚠️ Snack not found! ⚠️")

print("\nFinal snacks",snacks)
print("# of snacks",len(snacks))
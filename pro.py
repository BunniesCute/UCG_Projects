

col = int(input("Enter amount of columns: "))
row = int(input("\nEnter amount of rows: "))
sym = input("\nEnter symbol to use (*,@,#,etc): ")

for i in range(row):
    for j in range(col):
        print(f"{sym}", end=" ")
    print()

print("🎉 Pattern Comptete")
print(f"You made a {col} x {row} pattern using '{sym}'!")
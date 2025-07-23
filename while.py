
print("="*50)

count = 1

while count <= 5:
    print(f"Count is: {count}")
    count = count + 1

print("Loop finished count is now", count)

print("="*50)

codown = 10

while codown > 0:
    print(f"Countdown: {codown}")
    codown -= 1

print("🚀 BLAST OFF!!! ")

print("="*50)

password = ""

while password != "Python":
    password = input("Enter password: ")

    if password != "Python":
        print("Wrong Try again")

    print("Correct")

    print("="*50)

total = 0
num = 1

print("Enter to add 0 to stop")

while num != 0:
    num = int(input("Enter number: "))

    if num != 0:
        total = total + num
        print(f"Total: {total}")
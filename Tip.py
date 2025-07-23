
print("="*50)

bill = float(input("Enter bill amount: $"))

tip = float(input("Put in wanted tip amount: "))

totaltip = (tip/100) * bill                                                                         

totalamount = totaltip + bill

#print("This is the bill: " , bill)
#print("This is tip amount: " , totaltip)
#print("This is the total bill: ", totalamount )

print(f"Bill: {bill:.2f}")

print(f"Tip: ",totaltip)

print(f"Total: ",totalamount)

print("Thank you for using this service.")

print("="*50)




print("="*50)

itemprice = float(input("\nEnter price of item: $"))

Tax = 8.25

totalTaxAmount = Tax/100 * itemprice

totalAmount = itemprice + totalTaxAmount 

print(f"Item Price: {itemprice:.2f}")

print(f"Sales Tax (8.25%): ",totalTaxAmount)

print(f"Total Cost: ",totalTaxAmount+itemprice)

print(f"\nThank you for using this service.")

print("="*50)

# Scenario-based challenge :- shopping cart total calculator
# Write a Python program that simulates a simple shopping cart total calculator.
item_name=input("Enter the item name: ")
Price_per_item=float(input("Enter the price per item: "))
Quantity=int(input("Enter the quantity: "))

Subtotal=Price_per_item*Quantity
Tax_rate=5/100*Subtotal
Total=Subtotal+Tax_rate

print(f"----Receipt----\nItem: {item_name}\nPrice per item: ${Price_per_item}\nQuantity: {Quantity}\nSubtotal: ${Subtotal}\nTax: ${Tax_rate}\nTotal: ${Total}\n----------------")

# OUTPUT:
# Enter the item name: Wireless mouse
# Enter the price per item: 25.50
# Enter the quantity: 3
# ----Receipt----
# Item: Wireless mouse
# Price per item: $25.5
# Quantity: 3
# Subtotal: $76.5  
# Tax: $3.825
# Total: $80.325
# ----------------

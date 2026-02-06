# E-commerce checkout with Change 


item1=input("Enter item1  Name : ")
Item1_price=int(input("Item_1_price :- $"))
item2=input("Enter item2  Name : ")
Item2_price=int(input("Item_2_price :- $"))
item3=input("Enter item3  Name : ")
Item3_price=int(input("Item_3_price :- $"))

payement=int(input("give your payement in cash :- $"))
print("\n")

expediture=Item1_price+Item2_price+Item3_price
tax=0.1*expediture
bill=expediture+tax
Change=payement-bill

print(f"-----------receipt------------\n")
print(f"{item1}----------${Item1_price}")
print(f"{item2}----------${Item2_price}")
print(f"{item3}----------${Item3_price}")
print(f"payement----------${payement}")
print(f"Expediture----------${expediture}")
print(f"bill including Tax--${bill}")
print(f"change----------${Change}")
print("----------------------------------")


# output:
# Enter item1  Name : mouse
# Item_1_price :- $25
# Enter item2  Name : keyboard
# Item_2_price :- $25
# Enter item3  Name : monitor
# Item_3_price :- $25
# give your payement in cash :- $100


# -----------receipt------------

# mouse----------$25
# keyboard----------$25
# monitor----------$25
# payement----------$100
# Expediture----------$75
# bill including Tax--$82.5
# change----------$17.5
# ----------------------------------





#simple Finance Tool
Principal=int(input("Enter the principal amount: "))
Rate=float(input("Enter the rate of interest: "))
Time=int(input("Enter the time in years: "))

Simple_Interest=(Principal*Rate*Time)/100
Total_Amount=Principal+Simple_Interest
print(f"The Simple Interest is: {Simple_Interest}")
print(f"The Total Amount is: {Total_Amount}")


# OUTPUT:
# Enter the principal amount: 1000
# Enter the rate of interest: 5
# Enter the time in years: 3
# The Simple Interest is: 150.0
# The Total Amount is: 1150.0
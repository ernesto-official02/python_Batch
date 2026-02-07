print("Scholarship-filter-checker")
student=input("enter your name: ")
cgpa=float(input("Enter your current cgpa : "))
income=int(input("Enter your Family-income : "))
sports_interest=input("if you are a sports_prodigy respond : (yes/no): ")=='yes'

result = cgpa>3.5 and income<20000 or sports_interest

print(f"{student}'s eligibility : - {result}")


# output :-
# Scholarship-filter-checker
# enter your name: Ernest
# Enter your current cgpa : 3.6
# Enter your Family-income : 21000
# if you are a sports_prodigy respond : (yes/no): no
# Ernest's eligibility : - False

# Scholarship-filter-checker
# enter your name: Ernest
# Enter your current cgpa : 3.6
# Enter your Family-income : 19000
# if you are a sports_prodigy respond : (yes/no): no
# Ernest's eligibility : - True
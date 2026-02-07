print("Membership-checker")

banned_usernames=['admin','root','dev']

new_user=input('enter your username - ')


result=new_user.lower() not in banned_usernames

print(f"'{new_user}' is-safe :- {result}")

# output:-
# Membership-checker
# enter your username - dev
# 'adMin' is-safe :- False

# Membership-checker
# enter your username - ernest
# 'adMin' is-safe :- True


# Membership-checker
# enter your username - adMin
# 'adMin' is-safe :- False
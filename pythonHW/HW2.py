#  Estimating the risk of death from coronavirus.
#  Write a program that takes "Yes" or "No" from the users to answer:
#  1. Are you a cigarette addict older than 75 years old?
#  2. Do you have a severe chronic disease?
#  3. Is your immune system too weak?
#  Use boolean operators and if-statements to determine:
#  risky (if True) not risky (if False)

age = input("Are you a cigarette addict older than 75 years old? (Yes or No) ").lower()
chronic = input("Do you have a severe chronic disease? (Yes or No) ").lower()
immune = input("Is your immune system weakened? (Yes or No) ").lower()

if (age == "yes") or (chronic == "yes") or (immune == "yes"):
    print("You are in risky group.")
else:
    print("You are not in risky group.")

# we have phone balance of 20 Rs.

phone_balance = 30

bank_balance = 1000

print("How many minutes did you speak")

minutes = int(input())

# Since one minute costs 1 rupee
phone_balance = phone_balance - minutes

if phone_balance<5:
	phone_balance+=10
	bank_balance-=10


print("The new phone balance is ",phone_balance)
print("The new bank account balance is ",bank_balance)




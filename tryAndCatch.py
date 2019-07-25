# In order to execute the following program
# We are going to use a Try and Catch Block

balance = 5000
try:

	print("Enter the withdrawl amount")

	withdrawl = int(input())

	balance = balance - withdrawl

	print("You have withdrawn Rs ",withdrawl)

except:

	print("Invalid input\nPlease enter a integer")

finally:

	print("The remaining balance is: Rs ",balance)

	


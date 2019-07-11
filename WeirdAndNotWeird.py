# get input n

n = int(input())

# 1<=n<=100

if 1<=n<=100:
	
	# We are checking if n is odd
	if n%2==1:
		print("Weird")
	# Else condition means that n is even
	else:
		if 2<=n and n<=5:
			print("Not Weird")

		#Next if condition
		# if n is between 6 to 20 "Weird"
		if 6<=n and n<=20:
			print("Weird")

		#if n > 20 . Print Not Weird
		if n>20:
			print("Not Weird")







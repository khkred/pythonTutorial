
try:

	print("Enter two numbers to find their division")

	a = int(input())

	b = int(input())

	c = a/b

	print("The division of {} and {} is {}".format(a,b,a/b))

except Exception as e:

	print("Your inputs do not work because:")
	print("We got the following Exception ",e)
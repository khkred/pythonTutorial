cast = {
"Jerry Seinfeld": "Jerry Seinfeld",
"Julia Louis-Dreyfus": "Elaine Benes", 
"Jason Alexander": "George Costanza", 
"Michael Richards": "Cosmo Kramer"
}

# Here we are printing key values
for key in cast:
	print(key)

# Now we want to print the pair values

for key,pair in cast.items():

	print(pair)

# We want to print both key and pair values

for key,pair in cast.items():

	print("Actor: ",key," Role: ",pair)








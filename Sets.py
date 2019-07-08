# Sets are immutable and unordered sequences

# WE have user Signup , we are taking their countries
# We got a total of 277 countries, in those cases we will use Sets

countries = ["India","USA","Russia","China","Egypt","Russia"]

unq_countries = set(countries)

print(unq_countries)

isIndiaAvailable = "India" in unq_countries

isRussiaAvailable = "Russia" in unq_countries

#Now we want to add Scotland to our countries list

unq_countries.add("Scotland")

print(unq_countries)

# We want to remove China from the set

unq_countries.pop()

print(unq_countries)













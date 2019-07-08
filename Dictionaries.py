elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

print("The atomic weight of helium is: ",elements["helium"])

elements["Oxygen"] = 8

print("Our Current Periodic table: ",elements)

print("The atomic weight of Oxygen is: ",elements["Oxygen"])

print("The atomic weight of hydrogen is: ",elements.get("hydrogen"))

# We want to find the atomic weight of Nitrogen

nitrogen = elements.get("nitrogen")

print(nitrogen is None)
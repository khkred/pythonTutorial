# Now we are looking at dictionaries inside dictionary

elements = {"hydrogen": {"number": 1, "weight": 1.00794,
"symbol": "H"},
"helium": {"number": 2, "weight": 4.002602,
"symbol": "He"}}

print(elements["hydrogen"])

hydrogen_symbol = elements["hydrogen"]["symbol"]

print("The symbol for hydrogen is: ",hydrogen_symbol)
# write your function here

def readable_timedelta(days):

	weeks = int(days/7)

	tempDays = days%7

	return str(weeks) + " week(s) and " + str(tempDays) + "day(s)"


# test your function
print(readable_timedelta(10))
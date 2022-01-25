# Team 1 BCE 2.2
# Quin Alexander, Annie Ho, Buki James, Joseph Santhosh, Jason Sun

# Task 1: Calculate (using variables, rather than numeric constants) how many US dollars one currently has if one has 1,000,000 Venezuelan Bolivars
conversionRate = 0.016
bolivarToUS = 1000000 * conversionRate
print('1,000,000 Bolivars is equal to %f dollars' % bolivarToUS)

# Task 2: Calculate how many Bolivars you would need to have today to live for the next 3 years if you require $12,060 (US) per year, and you keep the sum in cash under your mattress
threeYearsMoney = 3 * 12060
usToBolivar = threeYearsMoney / conversionRate
print('%f Bolivars needed for 3 years of living' % usToBolivar)

# Task 3: Calculate how many minutes there will be in the next 3 years, if there are 365.2425 days in a year. Calculate how many Bolivars you would spend per minute, on average
daysInThreeYears = 3 * 365.2425
minutesInThreeYears = (daysInThreeYears * 24) * 60
print('%f Bolivars spent per minute within three years of living' % (usToBolivar / minutesInThreeYears))

# Task 4: Create the variable, bloody_vikings, containing the value ‘Wonderful Spam! Glorious Spam!’
bloody_vikings = 'Wonderful Spam! Glorious Spam!'

# Task 5: Create a variable, viking_exclamations, containing a two-item list of the values of the two exclamations in bloody_vikings.
viking_exclamations = ['Wonderful Spam!', 'Glorious Spam!']

# Task 6: Create a variable, viking_exaggeration, containing the second value in the list assigned to viking_exclamations.
viking_exaggeration = viking_exclamations[1]

# Task 7: Create a variable, upper_exaggeration, containing the completely capitalized (not just the first letter) version of the contents of viking_exaggeration
upper_exaggeration = [x.upper() for x in viking_exclamations]

# Task 8: Create a variable, partial_exaggeration, containing the 4th through 8th characters of the string assigned to viking_exaggeration.
partial_exaggeration = viking_exaggeration[3:8]
# Team 1 BCE 4.2
# Quin Alexander, Annie Ho, Buki James, Joseph Santhosh, Jason Sun


# 1. Accept two command line arguments (following the name of the program file):
#       the day (e.g., Sunday, Monday…) and
#       the meal (breakfast, lunch, dinner). 

import sys

# Dictionary specialsMenu that stores a dictionary for each day with each day's special
specialsMenu = {
    'Sunday': {
        'breakfast': 'scones',
        'lunch': 'quesadillas',
        'dinner': 'veg lasagna'
    },
    'Monday': {
        'breakfast': 'oatmeal',
        'lunch': 'veg burgers',
        'dinner': "veg chilli"
    },
    'Tuesday': {
        'breakfast': 'pancakes',
        'lunch': 'salad',
        'dinner': 'veg curry'
    },
    'Wednesday': {
        'breakfast': 'croissants',
        'lunch': 'burritos',
        'dinner': 'pad thai'
    },
    'Thursday': {
        'breakfast': 'waffles',
        'lunch': 'calzones',
        'dinner': 'pizza'
    },
    'Friday': {
        'breakfast': 'brownies',
        'lunch': 'veg kabobs',
        'dinner': 'broccoli quiche'
    },
    'Saturday': {
        'breakfast': 'eggs',
        'lunch': 'tortas',
        'dinner': 'penne with pesto'
    }
}

# 2. Use the two arguments to look up the special. Print out a statement about these things, similar to “The special for Friday dinner will be broccoli quiche.” 

day = sys.argv[1]
time = sys.argv[2]

print('The special for %s %s is %s.' % (day, time, specialsMenu[day][time]))

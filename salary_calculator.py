#!/usr/bin/env python3

#
# File:         salary_calculator.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         11/10/2021
# Description:  Calculate how much a user will get paid after a day, week,
#               month, or year.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#


# Variable initialisation.
salary_per_hour = float(input('How much do you get paid per hour: '))

hours_per_day = float(input('How many hours do you work per day: '))
while not 0 <= hours_per_day <= 24:             # Hour input validation.
    print('Error: Invalid hour value')
    hours_per_day = float(input('How many hours do you work per day: '))

duration = input('Enter the duration to calculate (day/week/month/year): ')
while duration not in ['day', 'week', 
                       'month', 'year']:        # Duration input validation.
    print('Error: Invalid duration')
    duration = input('Enter the duration to calculate (day/week/month/year): ')


# Now that we have a valid duration (day/week/month/year)
# calculate the salary based on the user input duration.

if duration == 'day': # Calculate the salary earned per day.
    print(f'After a day you\'ll earn ${salary_per_hour * hours_per_day}')

else:
    # Now that duration is either week/month/year
    # prompt the user for days spent working per week.
    days_per_week = int(input('How many days do you work per week: '))
    while days_per_week not in range(8):        # Day input validation.
        print('Error: Invalid day value')
        days_per_week = int(input('How many days do you work per week: '))

    # Initialisa a variable representing a common operation.
    long_term_salary = salary_per_hour * hours_per_day * days_per_week

    # Calculate the salary earned per week/month/year.
    if duration == 'week':
        print(f'After a {duration} you\'ll earn ${long_term_salary}')

    elif duration == 'month':
        print(
            f'After a {duration} you you\'ll between ${long_term_salary * 4}'
            f' and ${long_term_salary * 4.34524 : .2f}')

    else:
        print(
            f'After a {duration} you\'ll earn between ${long_term_salary * 48}'
            f' and ${long_term_salary * 52.1329 : .2f}')

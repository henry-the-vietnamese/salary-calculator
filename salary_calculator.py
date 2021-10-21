#!/usr/bin/env python3

#
# File:         salary_calculator.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         11/10/2021
# Description:  Calculate how much a user will get paid after a day, week, month, or year.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#


# Variable initialisation.
SALARY_PER_HOUR = float(input('How much do you get paid per hour: '))

HOURS_PER_DAY = float(input('How many hours do you work per day: '))
while not 0 <= HOURS_PER_DAY <= 24:             # Hour input validation.
    print('Error: Invalid hour value')
    HOURS_PER_DAY = float(input('How many hours do you work per day: '))

duration = input('Enter the duration to calculate (day/week/month/year): ')
while duration not in ['day', 'week', 
                       'month', 'year']:        # Duration input validation.
    print('Error: Invalid duration')
    duration = input('Enter the duration to calculate (day/week/month/year): ')


# Now that we have a valid duration (day/week/month/year)
# calculate the salary based on the user input duration.

if duration == 'day': # Calculate the salary earned per day.
    print(f'After a day you will earn ${SALARY_PER_HOUR * HOURS_PER_DAY}')

else:
    # Now that duration is either week/month/year
    # prompt the user for days spent working per week.
    DAYS_PER_WEEK = int(input('How many days do you work per week: '))
    while DAYS_PER_WEEK not in range(8):        # Day input validation.
        print('Error: Invalid day value')
        DAYS_PER_WEEK = int(input('How many days do you work per week: '))

    # Initialisa a variable representing a common operation.
    LONG_TERM_SALARY = SALARY_PER_HOUR * HOURS_PER_DAY * DAYS_PER_WEEK

    # Calculate the salary earned per week/month/year.
    if duration == 'week':
        print(f'After a {duration} you will earn ${LONG_TERM_SALARY}')

    elif duration == 'month':
        print(f'After a {duration} you will earn between ${LONG_TERM_SALARY * 4} \
and ${round(LONG_TERM_SALARY * 4.34524, 2)}')

    else:
        print(f'After a {duration} you will earn between ${LONG_TERM_SALARY * 48} \
and ${round(LONG_TERM_SALARY * 52.1329, 2)}')

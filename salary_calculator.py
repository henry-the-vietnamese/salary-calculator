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

# Set the initial values.
SALARY_PER_HOUR = int(input('How much do you get paid per hour: '))
HOURS_PER_DAY = int(input('How many hours do you work per day: '))
duration = input('Enter the duration to calculate (day/week/month/year): ')

# Duration input validation.
if duration not in ['day', 'week', 'month', 'year']:
    print('Error: Invalid duration')
else:
    """
    The duration is valid: belongs to one of the four - day/week/month/year.
    Now calculate the salary based on the user input duration.
    """
    if duration == 'day':
        print(f'After a day you will earn ${SALARY_PER_HOUR * HOURS_PER_DAY}')
    else:
        DAYS_PER_WEEK = int(input('How many days do you work per week: '))
        if duration == 'week':
            print(f'After a {duration} you will earn ${SALARY_PER_HOUR * HOURS_PER_DAY * DAYS_PER_WEEK}')
        elif duration == 'month':
            print(f'After a {duration} you will earn between ${SALARY_PER_HOUR * HOURS_PER_DAY * DAYS_PER_WEEK * 4} and ${round(SALARY_PER_HOUR * HOURS_PER_DAY * DAYS_PER_WEEK * 4.34524, 2)}')
        else:
            print(f'After a {duration} you will earn between ${SALARY_PER_HOUR * HOURS_PER_DAY * DAYS_PER_WEEK * 48} and ${round(SALARY_PER_HOUR * HOURS_PER_DAY * DAYS_PER_WEEK * 52.1329, 2)}')

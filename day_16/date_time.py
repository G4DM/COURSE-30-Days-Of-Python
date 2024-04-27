from day16_module import now, year, month, day, hour, minute, second, timestamp
from datetime import datetime

# Exercise 1: get the current day, month, year, hour, minute and timestamp from datetime module.

def exercise1():
    formatted = f'Current day: {day}, month: {month}, hour: {hour}, minute: {minute} and timestamp: {timestamp}.'
    return formatted

print(exercise1())

# Exercise 2: Format the current date using this format: "%m/%d/%Y, %H:%M:%S"

print(now.strftime("%m/%d/%Y, %H:%M:%S"))

# Exercise 3: Today is 5 December, 2019. Change this time string to time.

string_to_time = datetime.strptime("5 December, 2019", "%d %B, %Y").time()

print(string_to_time)

# Exercise 4: Calculate the time difference between now and new year

new_year = datetime(year = 2025, month = 1, day = 1)
today = now

print(new_year - today)

# Exercise 5: Calculate the time difference between 1 January 1970 and now

jan_1_1970 = datetime(year = 1970, month = 1, day = 1)

print(today - jan_1_1970)